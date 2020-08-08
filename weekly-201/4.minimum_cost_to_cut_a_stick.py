"""
https://leetcode.com/contest/weekly-contest-201/problems/minimum-cost-to-cut-a-stick/
"""
import functools


class MySolution:
    """Brute force. Got TLE on #93/100."""
    def minCost(self, n: int, cuts: List[int]) -> int:
        @functools.lru_cache(None)
        def helper(n, cuts):
            if len(cuts) == 0:
                return 0
            if len(cuts) == 1:
                return n
            res = math.inf
            for i, v in enumerate(cuts):
                res = min(
                    res,
                    n + helper(v, cuts[:i]) + helper(n-v, tuple(t-v for t in cuts[i+1:]))
                )
            return res

        cuts.sort()
        return helper(n, tuple(cuts))


class Solution:
    """O(n^3). DP. Similar to Matrix Multiplication."""
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        l = len(cuts)
        dp = [[0] * l for _ in range(l)]
        for d in range(2, l):
            for i in range(l - d):
                dp[i][i+d] = min(dp[i][m] + dp[m][i+d] for m in range(i+1, i+d)) + cuts[i+d] - cuts[i]
        return dp[0][l-1]
