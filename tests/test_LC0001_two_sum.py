import pytest

from solutions.easy.LC0001_two_sum import (
    SolutionBruteForce,
    SolutionHashMap,
    SolutionTwoPointers,

)

SOLUTIONS = [
    SolutionBruteForce,
    SolutionHashMap,
    SolutionTwoPointers,
]

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, {0, 1}),
    ([3, 2, 4], 6, {1, 2}),
    ([3, 3], 6, {0, 1}),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_two_sum(SolutionCls, nums, target, expected):
    res = SolutionCls().twoSum(nums, target)
    assert set(res) == expected
