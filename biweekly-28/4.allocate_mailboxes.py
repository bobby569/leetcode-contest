"""
https://leetcode.com/contest/biweekly-contest-28/problems/allocate-mailboxes/
"""
import math
from functools import lru_cache


class ACSolution:
    """DP. 452ms. 16.2M."""
    def minDistance(self, houses: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return math.inf
            return min(costs[i][j] + dp(k-1, j+1) for j in range(i, n))

        n, houses = len(houses), sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n-1):
            for j in range(n):
                median = houses[i+j >> 1]
                # minimal total distance for [i:j+1] house if placed one mailbox
                costs[i][j] = sum(abs(median - houses[t]) for t in range(i, j+1))
        return dp(k, 0)
