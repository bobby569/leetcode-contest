"""
https://leetcode.com/contest/weekly-contest-197/problems/number-of-substrings-with-only-1s/
"""


class Solution:
    def numSub(self, s: str) -> int:
        ones = [c for c in s.split('0') if c]
        return sum(len(c) * (len(c) + 1) // 2 for c in ones) % 1000000007
