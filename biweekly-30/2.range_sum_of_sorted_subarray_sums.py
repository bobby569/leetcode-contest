"""
https://leetcode.com/contest/biweekly-contest-30/problems/range-sum-of-sorted-subarray-sums/
"""


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res, l = [], len(nums)
        for i in range(l):
            tmp = 0
            for j in range(i, l):
                tmp += nums[j]
                res.append(tmp)
        res.sort()
        return sum(res[left-1:right]) % 1000000007
