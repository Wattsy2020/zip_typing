from typing import TYPE_CHECKING, Iterable, TypeVar, cast

T = TypeVar("T", int, float)


# unfortunately have to say the return type can be a literal[0], or use cast, for the empty list case
# haskell can handle this perfectly fine with the below code type checking well:
# sum' :: (Num a) => [a] -> a
# sum' [] = 0
# sum' (x : xs) = x + sum' xs
def sum_(nums: Iterable[T]) -> T:
    """Return the sum of an iterable"""
    nums = list(nums)
    match nums:
        case []:
            return cast(T, 0)
        case x, *xs:
            result: T = x
            for x in xs:
                result += x
            return result
        case other:
            raise ValueError(f"Invalid input {other=}")


input1 = [1, 2, 3]
input2 = [1.1, 2.2, 3.3]
result1 = sum_(input1)
result2 = sum_(input2)
result3 = sum_([])

if TYPE_CHECKING:
    reveal_type(result1)
    reveal_type(result2)
    reveal_type(result3)
