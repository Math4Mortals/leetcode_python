import pytest

from solutions.easy.LC0217_contains_duplicate import (
    SolutionDict,
    SolutionSet,
)


SOLUTIONS = [
    SolutionDict,
    SolutionSet,
]


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
    ([1,2,3,4,5,6,7,8,9,10], False),
    ([1], False),
])
@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_lc0217_contains_duplicate(SolutionCls, nums, expected):
    res = SolutionCls().containsDuplicate(nums)
    assert res == expected
