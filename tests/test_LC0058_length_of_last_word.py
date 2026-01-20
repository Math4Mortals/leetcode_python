import pytest

from solutions.easy.LC0058_length_of_last_word import (
    SolutionLastIndex,
    SolutionOneString,
)

SOLUTIONS = [
    SolutionLastIndex,
    SolutionOneString,
]


@pytest.mark.parametrize("string, expected_len", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_length_of_last_word(SolutionCls, string, expected_len):
    res = SolutionCls().lengthOfLastWord(string)
    assert res == expected_len
