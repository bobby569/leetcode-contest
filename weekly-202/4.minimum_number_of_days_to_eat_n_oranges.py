"""
https://leetcode.com/contest/weekly-contest-202/problems/minimum-number-of-days-to-eat-n-oranges/
"""
import math


class Solution:
    """O(n). Got TLE on #96/176."""
    def minDays(self, n: int) -> int:
        dp = [0,1,2,2,3] + [0] * (n-4)
        for i in range(5, len(dp)):
            a = dp[i - 1]
            b = dp[i // 2] if i & 1 == 0 else math.inf
            c = dp[i // 3] if i % 3 == 0 else math.inf
            dp[i] = min(a, b, c) + 1
        return dp[n]


class ACSolution1:
    """DP. 64ms."""
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 4:
            return (n >> 1) + 1
        a = self.minDays(n // 2) + n % 2
        b = self.minDays(n // 3) + n % 3
        return min(a, b) + 1


class ACSolution2:
    """BFS. 6344ms."""
    def minDays(self, n: int) -> int:
        days, level, seen = 0, {n}, {n}
        while level:
            tmp = set()
            for n in level:
                tmp |= {l-1 for l in level} - seen
                tmp |= {l // 2 for l in level if l % 2 == 0} - seen
                tmp |= {l // 3 for l in level if l % 3 == 0} - seen
            days += 1
            if 0 in tmp:
                return days
            seen |= tmp
            level = tmp
