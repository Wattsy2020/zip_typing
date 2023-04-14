"""Does the typing work with a normal function that zips? Yes of course"""
from typing import Iterable, TYPE_CHECKING

def zip_func(a: Iterable[int], b: Iterable[str]) -> list[tuple[int, str]]:
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
