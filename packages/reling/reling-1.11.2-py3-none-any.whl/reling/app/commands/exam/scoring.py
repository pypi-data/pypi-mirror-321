from itertools import islice
from typing import cast, Generator

from lcs2 import lcs_indices

from reling.app.exceptions import AlgorithmException
from reling.config import MAX_SCORE
from reling.db.enums import ContentCategory
from reling.db.models import Language
from reling.gpt import GPTClient
from reling.helpers.scoring import calculate_diff_score
from reling.types import DialogueExchangeData, Promise
from reling.utils.english import pluralize
from reling.utils.iterables import group_items
from reling.utils.transformers import add_numbering, apply, omit_empty, remove_numbering, strip
from .types import ExchangeWithTranslation, PreScoreWithSuggestion, ScoreWithSuggestion, SentenceWithTranslation

__all__ = [
    'score_dialogue_translations',
    'score_text_translations',
]

NA = 'N/A'
EMPTY_TRANSLATION = '<empty>'


def build_prompt_translation(
        category: ContentCategory,
        source_language: Language,
        target_language: Language,
        blocks: list[str],
        translations: list[str | None],
) -> str:
    """Build a prompt for scoring translations."""
    # Speaker turns in dialogues are "graded" as well so that the model appreciates the context.
    n = len(blocks)
    return '\n'.join([
        f'Below {'is' if n == 1 else 'are'} {n} {pluralize('sentence', n)} from a {category.value} '
        f'in {source_language.name} along with {'its' if n == 1 else 'their'} {pluralize('translation', n)} '
        f'into {target_language.name} made by a language learner.',

        f'Score {'the' if n == 1 else 'each'} translation on a scale from 0 to {MAX_SCORE}. '
        f'If {'the' if n == 1 else 'a'} translation is empty, very short, or poor, assign a low score. ',
        f'If the translation is less than perfect, suggest a minimally modified version that would '
        f'deserve a {MAX_SCORE}.',

        f'{'Provide' if n == 1 else 'For each translation, provide'} your feedback on exactly four lines '
        f'(without adding bullet points or dashes in front of them):',
        f'- original sentence on the first line;',  # The first two lines help improve the model's performance
        f'- learner\'s translation on the second line;',
        f'- score (just the number) on the third line;',
        f'- suggested modified translation (or "{NA}") on the fourth line (do not enclose it in quotes).',

        *([f'Provide this feedback for each of the {n} translations.'] if n > 1 else []),
        f'Say nothing else.',
        f'',
        f'The original {category.value} is:',
        *apply(add_numbering, blocks),
        f'',
        f'The translations are:',
        *apply(add_numbering, [translation or EMPTY_TRANSLATION for translation in translations]),
    ])


def parse_scoring(string_score: str, suggestion: str) -> PreScoreWithSuggestion:
    """
    Parse the score and suggestion from the model output.
    :raises AlgorithmException: If there is an issue with the output of the model.
    """
    try:
        score = int(string_score)
    except ValueError:
        raise AlgorithmException(f'Could not parse the score as an integer from the model output: {string_score}.')
    if score < 0 or score > MAX_SCORE:
        raise AlgorithmException(f'The score {score} given by the model is not in the range from 0 to {MAX_SCORE}.')
    return PreScoreWithSuggestion(
        score=score,
        suggestion=(suggestion or None) if suggestion != NA else None,
    )


def ask_and_parse_translation(gpt: GPTClient, prompt: str) -> Generator[PreScoreWithSuggestion, None, None]:
    """
    Ask the model to score translations and parse the output.
    :raises AlgorithmException: If there is an issue with the output of the model.
    """
    for _, _, string_score, suggestion in group_items(gpt.ask(
        prompt,
        creative=False,
        transformers=[strip, omit_empty, remove_numbering],
    ), 4):
        yield parse_scoring(string_score, suggestion)


def build_prompt_averaging(language: Language, sentence: str, a: str, b: str) -> str:
    """Build a prompt for scoring an "averaged" translation."""
    return '\n'.join([
        f'Below are two nearly identical sentences in {language.name}:',

        add_numbering(a, 0),
        add_numbering(b, 1),

        f'A learner of {language.name} briefly viewed both sentences and was then asked to reproduce a similar '
        f'sentence from memory. The learner\'s response is provided below:',

        f'"""{sentence}"""',

        f'Score the learner\'s response on a scale from 0 to {MAX_SCORE}. Deduct points if the response contains '
        f'grammatical errors or does not convey the same meaning as the original sentences.',

        f'If the response is less than perfect, suggest a minimally modified version of it that would deserve a score '
        f'of {MAX_SCORE}.',

        f'Provide your feedback on exactly two lines (without adding bullet points or dashes in front of them):',
        f'- the score (just the number) on the first line;',
        f'- the suggested improved response (or "{NA}") on the second line (do not enclose it in quotes).',
    ])


def ask_and_parse_averaging(gpt: GPTClient, prompt: str) -> PreScoreWithSuggestion:
    """
    Ask the model to score an "averaged" translation and parse the output.
    :raises AlgorithmException: If there is an issue with the output of the model.
    """
    for string_score, suggestion in group_items(gpt.ask(
            prompt,
            creative=False,
            transformers=[strip, omit_empty, remove_numbering],
    ), 2):
        return parse_scoring(string_score, suggestion)


def lcs_indices_a(a: str, b: str) -> set[int | tuple[int, int]]:
    """
    Return a set of indices and consecutive index pairs in `a` that are part of the longest common subsequence with `b`.
    Consecutive index pairs are included only if the corresponding indices in `b` are also consecutive.
    """
    result: set[int | tuple[int, int]] = set()
    last_a_index = last_b_index = None
    for a_index, b_index in lcs_indices(a, b):
        result.add(a_index)
        if last_a_index == a_index - 1 and last_b_index == b_index - 1:
            result.add((last_a_index, a_index))
        last_a_index, last_b_index = a_index, b_index
    return result


def finalize_scoring(provided_translation: str, score: PreScoreWithSuggestion) -> ScoreWithSuggestion:
    """
    Return the highest score among the original score and the score calculated
    using the diff between the provided translation and the suggested translation;
    clear the suggestion if it is the same as the provided translation or the score is 0.
    """
    final_score = max([score.score] + ([calculate_diff_score(score.suggestion, provided_translation)]
                                       if score.suggestion is not None and provided_translation != '' else []))
    return ScoreWithSuggestion(
        score=final_score,
        suggestion=score.suggestion if score.suggestion != provided_translation and final_score > 0 else None,
    )


def fix_scoring(
        gpt: GPTClient,
        language: Language,
        provided_translation: str,
        original_translation: str,
        score: PreScoreWithSuggestion,
) -> ScoreWithSuggestion:
    """
    Fix the scoring by comparing the provided translation with the original translation and the suggested translation.
    """
    return finalize_scoring(
        provided_translation,
        score if (score.suggestion is None
                  # If the provided translation shares as much or more common characters (individual indices)
                  # and omissions (pairs of consecutive indices) with the suggestion as with the original translation,
                  # proceed with the current score; otherwise, recalculate the score using "averaging":
                  or lcs_indices_a(provided_translation, score.suggestion)
                  >= lcs_indices_a(provided_translation, original_translation))
        else ask_and_parse_averaging(
            gpt,
            build_prompt_averaging(language, provided_translation, a=original_translation, b=score.suggestion),
        ),
    ) if provided_translation != original_translation else ScoreWithSuggestion(
        score=MAX_SCORE,
        suggestion=None,
    )


def score_text_translations(
        gpt: Promise[GPTClient],
        sentences: list[SentenceWithTranslation],
        original_translations: list[str],
        source_language: Language,
        target_language: Language,
        offline: bool,
) -> Generator[ScoreWithSuggestion | None, None, None]:
    """
    Score the translations of a text and provide suggestions for improvement.
    :raises AlgorithmException: If there is an issue with the scoring algorithm.
    """
    if offline:
        for sentence, original_translation in zip(sentences, original_translations):
            yield ScoreWithSuggestion(
                score=calculate_diff_score(sentence.translation.text, original_translation),
                suggestion=original_translation,
            ) if sentence.translation else None
    else:
        client = gpt()
        prompt = build_prompt_translation(
            category=ContentCategory.TEXT,
            source_language=source_language,
            target_language=target_language,
            blocks=[cast(str, sentence.sentence) for sentence in sentences],
            translations=[sentence.translation.text if sentence.translation else None for sentence in sentences],
        )
        for sentence, original_translation, pre_score in zip(
                sentences,
                original_translations,
                ask_and_parse_translation(client, prompt),
        ):
            yield fix_scoring(
                client,
                target_language,
                sentence.translation.text,
                original_translation,
                pre_score,
            ) if sentence.translation else None


def score_dialogue_translations(
        gpt: Promise[GPTClient],
        exchanges: list[ExchangeWithTranslation],
        original_translations: list[DialogueExchangeData],
        source_language: Language,
        target_language: Language,
        offline: bool,
) -> Generator[ScoreWithSuggestion | None, None, None]:
    """
    Score the translations of user turns in a dialogue and provide suggestions for improvement.
    :raises AlgorithmException: If there is an issue with the scoring algorithm.
    """
    if offline:
        for exchange, original_translation in zip(exchanges, original_translations):
            yield ScoreWithSuggestion(
                score=calculate_diff_score(exchange.user_translation.text, original_translation.user),
                suggestion=original_translation.user,
            ) if exchange.user_translation else None
    else:
        client = gpt()
        prompt = build_prompt_translation(
            category=ContentCategory.DIALOGUE,
            source_language=source_language,
            target_language=target_language,
            blocks=[turn for exchange in exchanges for turn in exchange.exchange.all()],
            translations=[turn
                          for exchange, original_translation in zip(exchanges, original_translations)
                          for turn in [None, exchange.user_translation.text if exchange.user_translation else None]],
        )
        for exchange, original_translation, pre_score in zip(
                exchanges,
                original_translations,
                islice(ask_and_parse_translation(client, prompt), 1, None, 2),
        ):
            yield fix_scoring(
                client,
                target_language,
                exchange.user_translation.text,
                original_translation.user,
                pre_score,
            ) if exchange.user_translation else None
