import pytest

from solutions.easy.LC0026_remove_duplicates_from_sorted_array import (
    SolutionWhile,
    SolutionFor,
)

SOLUTIONS = [
    SolutionWhile,
    SolutionFor,
]


@pytest.mark.parametrize("nums, expected_len, expected_arr", [
    ([], 0, []),
    ([1], 1, [1]),
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_remove_duplicates(SolutionCls, nums, expected_len, expected_arr):
    nums = nums.copy()
    res = SolutionCls().removeDuplicates(nums)
    print(res, nums, expected_len, expected_arr)
    assert res == expected_len
    assert nums[:res] == expected_arr
