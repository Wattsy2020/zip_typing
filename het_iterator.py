from __future__ import annotations

from typing import TYPE_CHECKING, Iterator, TypeVar

if TYPE_CHECKING:
    T = TypeVar("T")
    _T1 = TypeVar("_T1")
    normal_iterator = tuple[T, "normal_iterator[T]" | None]


def iterate_normal(iterator: normal_iterator[_T1]) -> Iterator[_T1]:
    next_iter: normal_iterator[_T1] | None = iterator
    while next_iter is not None:
        val, next_iter = next_iter
        yield val


if __name__ == "__main__":
    iterator: normal_iterator[int] = (1, (2, (3, None)))
    for val in iterate_normal(iterator):
        print(val)
