"""
https://leetcode.com/contest/weekly-contest-193/problems/running-sum-of-1d-array/
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur, res = 0, []
        for n in nums:
            cur += n
            res.append(cur)
        return res
