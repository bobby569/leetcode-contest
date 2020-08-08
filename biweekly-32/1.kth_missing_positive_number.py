"""
https://leetcode.com/contest/biweekly-contest-32/problems/kth-missing-positive-number/
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        for i in range(1, 2001):
            if i not in s:
                k -= 1
            if k == 0:
                return i
