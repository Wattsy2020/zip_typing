"""Does the typing work with a generic function that zips? Yes"""
from typing import Iterable, TypeVar, TYPE_CHECKING

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def zip_func(a: Iterable[_T1], b: Iterable[_T2]) -> list[tuple[_T1, _T2]]:
    a = list(a)
    b = list(b)
    length = min(len(a), len(b))
    return [(a[i], b[i]) for i in range(length)]

ints = [1, 2]
strs = ["a", "b", "c"]
result = zip_func(ints, strs)
if TYPE_CHECKING:
    reveal_type(ints)
    reveal_type(strs)
    reveal_type(result)
print(result)

# The problem is that mixed tuples aren't interpreted well
# The (tuple[int, str], tuple[int, str]) has int and str squashed to their common type, giving: (Iterable[Object], Iterable[Object])
tuple1 = (1, "a")
tuple2 = (2, "b")
result1 = zip_func(tuple1, tuple2)
result2 = list(zip(tuple1, tuple2))

if TYPE_CHECKING:
    reveal_type(result1)
    reveal_type(result2)

print(result1)
print(result2)

# To solve this we need to write the generics differently 
def zip_(*iterables: tuple[_T1, _T2]) -> tuple[list[_T1], list[_T2]]:
    tuples = list(iterables)
    list1: list[_T1] = []
    list2: list[_T2] = []
    for elem1, elem2 in tuples:
        list1.append(elem1)
        list2.append(elem2)
    return list1, list2

result3 = zip_(tuple1, tuple2)

if TYPE_CHECKING:
    reveal_type(result3)
print(result3)