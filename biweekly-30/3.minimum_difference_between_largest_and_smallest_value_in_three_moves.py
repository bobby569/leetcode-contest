"""
https://leetcode.com/contest/biweekly-contest-30/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
"""


class Solution:
    def minDifference(self, A: List[int]) -> int:
        if len(A) <= 4:
            return 0
        A.sort()
        return min(A[-4] - A[0], A[-3] - A[1], A[-2] - A[2], A[-1] - A[3])
