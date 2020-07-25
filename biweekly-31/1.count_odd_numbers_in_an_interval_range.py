"""
https://leetcode.com/contest/biweekly-contest-31/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - (low | 1)) // 2 + 1
