from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Iterator, Tuple, TypeVar, TypeVarTuple

if TYPE_CHECKING:
    T = TypeVar("T")
    _T1 = TypeVar("_T1")
    normal_iterator = tuple[T, "normal_iterator[T]" | None]

FIRST_ITEM = TypeVar("FIRST_ITEM")
ITEMS = TypeVarTuple("ITEMS")


def iterate_normal(iterator: normal_iterator[_T1]) -> Iterator[_T1]:
    next_iter: normal_iterator[_T1] | None = iterator
    while next_iter is not None:
        val, next_iter = next_iter
        yield val


# concrete problem: given a tuple[int, str, bool], return an iterator of tuple[tuple[int, bool], tuple[str, bool], tuple[bool, bool]] where the bool is the truthiness value
# we know that given a "compile time type" of tuple[int, str, bool], the output type should be exactly as above, so we should be able to make an iterator over this
# This is a sketch of a class to solve that problem, TypeVarTuple isn't supported by mypy yet so mypy fails type checking, need to revisit this later
class HetIterator(Generic[*ITEMS]):
    # init assigns first_item and rem_items
    def __init__(self, items: Tuple[*ITEMS]) -> None:
        if not items:
            raise ValueError("Cannot have empty items")
        self.items = items

    def next_het(
        self: HetIterator[FIRST_ITEM, *ITEMS]
    ) -> tuple[tuple[FIRST_ITEM, bool], HetIterator[*ITEMS] | None]:
        first, *rem_items = self.items
        result = (first, bool(first))
        next_iter = HetIterator(tuple(rem_items)) if rem_items else None
        return result, next_iter


if __name__ == "__main__":
    iterator: normal_iterator[int] = (1, (2, (3, None)))
    for val in iterate_normal(iterator):
        print(val)

    het_iterator = HetIterator((1, "hello", False))
    next_iter = het_iterator
    for i in range(3):
        result, next_iter = next_iter.next_het()
        print(result)
