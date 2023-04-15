"""Implements a Zip that types the Iterable[tuple[_t1, _t2, _t3]] -> tuple[list[_t1], list[_t2], list[_t3]] case correctly"""
from typing import TypeVar, overload

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")


@overload
def zip_(*tuples: tuple[_T1]) -> tuple[tuple[_T1, ...]]:
    ...


@overload
def zip_(*tuples: tuple[_T1, _T2]) -> tuple[tuple[_T1, ...], tuple[_T2, ...]]:
    ...


@overload
def zip_(
    *tuples: tuple[_T1, _T2, _T3]
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...]]:
    ...


@overload
def zip_(
    *tuples: tuple[_T1, _T2, _T3, _T4]
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...]]:
    ...


@overload
def zip_(
    *tuples: tuple[_T1, _T2, _T3, _T4, _T5]
) -> tuple[
    tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...], tuple[_T5, ...]
]:
    ...


# Any more than 5 elements and we just leave the return type as Any
@overload
def zip_(*tuples: tuple) -> tuple[tuple, ...]:
    ...


def zip_(*tuples: tuple) -> tuple[tuple, ...]:
    """Zips any number of tuples together, with more accurate type info than stdlib's zip"""
    return tuple(tuple(elems[i] for elems in tuples) for i in range(len(tuples[0])))
