"""Does the typing work with a generic function that has overloads? Yes, so long as you are using the overloads where each type is explicitly spelled out"""
from typing import Iterable, TypeVar, overload, TYPE_CHECKING, Any

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

@overload
def zip_func(a: Iterable[_T1], /) -> list[tuple[_T1]]:
    ...

@overload
def zip_func(a: Iterable[_T1], b: Iterable[_T2], /) -> list[tuple[_T1, _T2]]:
    ...

@overload
def zip_func(a: Iterable[_T1], b: Iterable[_T2], c: Iterable[Any], /, *iters: Iterable[Any]) -> list[tuple[Any, ...]]:
    ...


def zip_func(*values: Iterable[Any]) -> list[Any]:
    lists = list(map(list, values))
    min_length = min(map(len, lists))
    return [
        tuple(list_i[i] for list_i in lists)
        for i in range(min_length)
    ]

ints = [1, 2, 3]
strs = ["a", "b", "c"]
floats = [1.1, 1.2, 1.3, 1.4]

result1 = zip_func(ints)
result2 = zip_func(ints, strs)
result3 = zip_func(ints, strs, floats)
if TYPE_CHECKING:
    reveal_type(ints)
    reveal_type(strs)
    reveal_type(result1)
    reveal_type(result2)
    reveal_type(result3)
print(result1)
print(result2)
print(result3)
