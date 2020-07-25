"""
https://leetcode.com/contest/biweekly-contest-31/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
"""


class Solution:
    """Got TLE #127/129."""
    def minNumberOperations(self, target: List[int]) -> int:
        def dfs(arr):
            if not arr:
                return 0
            res = min(arr)
            tmp = [n - res for n in arr]
            i = 0
            for j, n in enumerate(tmp):
                if n == 0:
                    res += dfs(tmp[i:j])
                    i = j + 1
            return res + dfs(tmp[i:j+1])

        return dfs(target)


class ACSolution:
    """O(n). 916ms."""
    def minNumberOperations(self, T: List[int]) -> int:
        res = pre = 0
        for cur in T:
            res += max(cur - pre, 0)
            pre = cur
        return res

        # one-liner
        return sum(max(b-a, 0) for a, b in zip(T, T[1:])) + T[0]
