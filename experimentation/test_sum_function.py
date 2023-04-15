import math
from itertools import permutations
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from sum_function import sum_

T = TypeVar("T", int, float)


def equals(a: T, b: T) -> bool:
    isnan = (math.isnan(x) for x in (a, b))
    if any(isnan):
        return all(isnan)
    return a == b


@given(st.one_of(st.lists(st.integers()), st.lists(st.floats())))
def test_sum_function(nums: list[int] | list[float]) -> None:
    print(nums)
    result = sum_(nums)
    assert all(
        equals(sum_(nums_i), result)
        for _, nums_i in zip(range(100), permutations(nums))
    )

    for i in range(len(nums)):
        assert equals(nums[i] + sum_((*nums[:i], *nums[i + 1 :])), result)
