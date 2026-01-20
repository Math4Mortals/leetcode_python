import pytest

from solutions.easy.LC0014_longest_common_prefix import (
    SolutionSortWords,
)

SOLUTIONS = [
    SolutionSortWords,
]

@pytest.mark.parametrize("strings, prefix", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    ([""], ""),
    ([], ""),
    (["", "bbb"], "")
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_longest_common_prefix(SolutionCls, strings, prefix):
    res = SolutionCls().longestCommonPrefix(strings)
    assert res == prefix
