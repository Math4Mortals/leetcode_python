import pytest

from solutions.easy.LC0070_climbing_stairs import (
    SolutionRecursiveMemoization,

)

SOLUTIONS = [
    SolutionRecursiveMemoization,
]


@pytest.mark.parametrize("n, ways", [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
])

@pytest.mark.parametrize("SolutionCls", SOLUTIONS)
def test_climbing_stairs(SolutionCls, n, ways):
    res = SolutionCls().climbStairs(n)
    assert res == ways