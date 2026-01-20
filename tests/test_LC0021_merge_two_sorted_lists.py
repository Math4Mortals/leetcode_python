import pytest

from tests.helpers_linked_list import build_linked_list, to_list
from solutions.easy.LC0021_merge_two_sorted_lists import (
    Solution,
)

SOLUTIONS = [
    Solution,
]


@pytest.mark.parametrize("a, b, expected", [
    ([], [], []),
    ([], [0], [0]),
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([5], [1, 2, 3], [1, 2, 3, 5]),
    ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def  test_merge_two_sorted_lists(SolutionCls, a, b, expected):
    list1 = build_linked_list(a)
    list2 = build_linked_list(b)

    res = SolutionCls().mergeTwoLists(list1, list2)
    assert to_list(res) == expected
