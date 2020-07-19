"""
https://leetcode.com/contest/weekly-contest-198/problems/water-bottles/
"""


class Solution:
    def numWaterBottles(self, B: int, E: int) -> int:
        total = empty = B
        while empty >= E:
            q, r = divmod(empty, E)
            total += q
            empty = q + r
        return total
