"""
https://leetcode.com/contest/weekly-contest-202/problems/minimum-operations-to-make-array-equal/
"""


class Solution:
    def minOperations(self, n: int) -> int:
        return sum(n - (2*i+1) for i in range(n//2))
