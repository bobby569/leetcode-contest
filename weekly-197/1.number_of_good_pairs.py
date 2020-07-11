"""
https://leetcode.com/contest/weekly-contest-197/problems/number-of-good-pairs/
"""
import collections


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return sum(f * (f-1) // 2 for _, f in c.items())
