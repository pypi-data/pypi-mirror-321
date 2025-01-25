from typing import Iterable, TypeVar

T = TypeVar("T")


def filter_falsy(iterable: Iterable[T]) -> list[T]:
    """Filters out falsy values from an iterable and returns a list."""
    return [item for item in iterable if item]


def filter_duplicate(iterable: Iterable[T]) -> list[T]:
    """Filter duplicate from list and preserve the order."""
    return list(dict.fromkeys(iterable).keys())
