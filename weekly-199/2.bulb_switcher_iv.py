"""
https://leetcode.com/contest/weekly-contest-199/problems/bulb-switcher-iv/
"""


class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        for n in target:
            res += res & 1 ^ int(n)
        return res
