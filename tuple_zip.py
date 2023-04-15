"""Implements a Zip that types the Iterable[tuple[_t1, _t2, _t3]] -> tuple[list[_t1], list[_t2], list[_t3]] case correctly"""
from typing import TYPE_CHECKING, Any, Iterable, TypeVar, overload

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")


# Overloads for the tuple version of Zip
# we need to type: ignore these to ignore the overlap with the normal zip typing
@overload
def zip_(*tuples: tuple[_T1]) -> tuple[tuple[_T1, ...]]:  # type: ignore
    ...


@overload
def zip_(*tuples: tuple[_T1, _T2]) -> tuple[tuple[_T1, ...], tuple[_T2, ...]]:  # type: ignore
    ...


@overload
def zip_(  # type: ignore
    *tuples: tuple[_T1, _T2, _T3]
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...]]:
    ...


@overload
def zip_(  # type: ignore
    *tuples: tuple[_T1, _T2, _T3, _T4]
) -> tuple[tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...]]:
    ...


@overload
def zip_(  # type: ignore
    *tuples: tuple[_T1, _T2, _T3, _T4, _T5]
) -> tuple[
    tuple[_T1, ...], tuple[_T2, ...], tuple[_T3, ...], tuple[_T4, ...], tuple[_T5, ...]
]:
    ...


# Any more than 5 elements and we just leave the return type as Any
@overload
def zip_(*tuples: tuple[Any, ...]) -> tuple[tuple[Any, ...], ...]:  # type: ignore
    ...


# Overloads for the normal version of zip that takes iterables
@overload
def zip_(__iter1: Iterable[_T1], /) -> tuple[tuple[_T1], ...]:
    ...


@overload
def zip_(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2], /
) -> tuple[tuple[_T1, _T2], ...]:
    ...


@overload
def zip_(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], /
) -> tuple[tuple[_T1, _T2, _T3], ...]:
    ...


@overload
def zip_(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
    /,
) -> tuple[tuple[_T1, _T2, _T3, _T4], ...]:
    ...


@overload
def zip_(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
    __iter5: Iterable[_T5],
    /,
) -> tuple[tuple[_T1, _T2, _T3, _T4, _T5], ...]:
    ...


@overload
def zip_(
    __iter1: Iterable[Any],
    __iter2: Iterable[Any],
    __iter3: Iterable[Any],
    __iter4: Iterable[Any],
    __iter5: Iterable[Any],
    __iter6: Iterable[Any],
    /,
    *iterables: Iterable[Any],
) -> tuple[tuple[Any, ...], ...]:
    ...


def zip_(*tuples: Iterable[Any]) -> tuple[tuple[Any, ...], ...]:
    """Zips any number of tuples together, with more accurate type info than stdlib's zip"""
    lists: list[Any] = list(map(list, tuples))
    min_length = min(map(len, lists))
    return tuple(tuple(list_i[i] for list_i in lists) for i in range(min_length))


# Now types for the tuple case are correctly inferred
tuple1 = (1, "a")
tuple2 = (2, "b")
result1 = zip_(tuple1, tuple2)
orig_result1 = tuple(zip(tuple1, tuple2))
if TYPE_CHECKING:
    reveal_type(result1)  # = tuple[tuple[int, ...], tuple[str, ...]]
    reveal_type(orig_result1)  # = tuple[tuple[Object, Object], ...]]

# Types for the original iterable case still work
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
result2 = zip_(list1, list2)
orig_result2 = tuple(zip(list1, list2))
if TYPE_CHECKING:
    reveal_type(result2)  # = tuple[tuple[int, str], ...]
    reveal_type(orig_result2)  # = tuple[tuple[int, str], ...]
