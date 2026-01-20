class SolutionRecursiveMemoization:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recursive(k: int) -> int:
            if k == 0:
                return 1
            elif k < 0:
                return 0
            if k in memo:
                return memo[k]

            memo[k] = recursive(k - 1) + recursive(k - 2)
            return memo[k]
        return recursive(n)
