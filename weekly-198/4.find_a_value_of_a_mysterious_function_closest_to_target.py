"""
https://leetcode.com/contest/weekly-contest-198/problems/find-a-value-of-a-mysterious-function-closest-to-target/

Came up with an equation that doesn't help at the end:
b = (a & b) ^ (a | b) ^ a
"""


class Solution:
    """O(n^2). 1848ms. Got TLE without the break."""
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res, n = math.inf, len(arr)
        for i in range(n):
            res, cur = min(res, abs(arr[i] - target)), arr[i]
            for j in range(i+1, n):
                cur &= arr[j]
                d = abs(cur - target)
                if res <= d:
                    # can break because & op can only make d larger afterwards
                    break
                res = d
        return res
