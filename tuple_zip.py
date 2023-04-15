"""Implements a Zip that types the Iterable[tuple[_t1, _t2, _t3]] -> tuple[list[_t1], list[_t2], list[_t3]] case correctly"""
from typing import TypeVar

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

# To solve this we need to write the generics differently 
def zip_(*iterables: tuple[_T1, _T2]) -> tuple[tuple[_T1, ...], tuple[_T2, ...]]:
    tuples = list(iterables)
    list1: list[_T1] = []
    list2: list[_T2] = []
    for elem1, elem2 in tuples:
        list1.append(elem1)
        list2.append(elem2)
    return tuple(list1), tuple(list2)
