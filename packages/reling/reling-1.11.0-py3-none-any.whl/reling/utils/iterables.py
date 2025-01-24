from typing import cast, Generator, Iterable

__all__ = [
    'extract_items',
    'group_items',
    'pair_items',
]


def group_items[T](iterable: Iterable[T], group_size: int) -> Generator[tuple[T, ...], None, None]:
    """
    Group items from the iterable into tuples of the specified size.
    The last tuple is discarded if it is shorter than the specified size.
    """
    items = iter(iterable)
    for item in zip(*(items for _ in range(group_size))):
        yield item


def pair_items[T](iterable: Iterable[T]) -> Generator[tuple[T, T], None, None]:
    """Pair items from the iterable into tuples. The last item is discarded if there is an odd number of items."""
    return cast(Generator[tuple[T, T], None, None], group_items(iterable, 2))


def extract_items[T](iterable: Iterable[T], indices: Iterable[int]) -> Generator[T, None, None]:
    """Extract items from the iterable by the specified indices."""
    index_set = set(indices)
    for index, item in enumerate(iterable):
        if index in index_set:
            yield item
