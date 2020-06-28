"""
https://leetcode.com/contest/biweekly-contest-29/problems/longest-subarray-of-1s-after-deleting-one-element/
"""


class Solution:
    """368ms."""
    def longestSubarray(self, nums: List[int]) -> int:
        arr, i = [], 0
        for j, v in enumerate(nums):
            if nums[i] != v:
                arr.append((j-i, nums[i]))
                i = j
        arr.append((j-i+1, nums[i]))
        if len(arr) == 1:
            return arr[0][0] - 1 if arr[0][1] else 0
        res, arr = 0, [(0,0)] + arr + [(0,0)]
        for i, (f, v) in enumerate(arr[1:-1], 1):
            if (f, v) == (1, 0):
                res = max(res, arr[i-1][0] + arr[i+1][0])
            if v == 1:
                res = max(res, f)
        return res


class Solution:
    """Another solution."""
    def longestSubarray(self, nums: List[int]) -> int:
        i, k = 0, 1
        for j, v in enumerate(nums):
            k -= v == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i
