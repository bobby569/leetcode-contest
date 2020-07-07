"""
https://leetcode.com/contest/weekly-contest-196/problems/can-make-arithmetic-progression-from-sequence/
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[0] - arr[1]
        return all(x-y == d for x, y in zip(arr, arr[1:]))
