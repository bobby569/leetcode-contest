"""
https://leetcode.com/contest/weekly-contest-195/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
"""


class ACSolution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # order does not matter
        MOD = 1000000007
        res, lo, hi = 0, 0, len(nums)-1
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                res += pow(2, hi-lo, MOD)
                lo += 1
        return res % MOD
