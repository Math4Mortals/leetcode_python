import pytest

from solutions.easy.LC0009_palindrome_number import (
    SolutionHalfReverse,
    SolutionFullReverse,
    SolutionSlice,
    SolutionMirrorIndexes
)

SOLUTIONS = [
    SolutionHalfReverse,
    SolutionFullReverse,
    SolutionSlice,
    SolutionMirrorIndexes
]

@pytest.mark.parametrize("x, expected", [
    (0, True),
    (7, True),
    (11, True),
    (121, True),
    (1324231, True),
    (123321, True),
    (10, False),
    (100, False),
    (12312452, False),
    (-121, False),
    (-10, False),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_palindrome_number(SolutionCls, x, expected):
    s = SolutionCls()
    assert s.isPalindrome(x) is expected