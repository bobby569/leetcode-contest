"""
https://leetcode.com/contest/weekly_contest_201/problems/maximum_number_of_non_overlapping_subarrays_with_sum_equals_target/
"""


class Solution:
    """O(nlogn). 1300ms."""
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        intv, dic, s = [], {0: -1}, 0
        for i, n in enumerate(nums):
            s += n
            ctp = s - target
            if ctp in dic:
                intv.append((dic[ctp], i))
            dic[s] = i

        intv.sort(key=lambda x: x[1])
        res, last = 0, -1
        for s, e in intv:
            if s >= last:
                res += 1
                last = e
        return res


class ACSolution:
    """O(n). 672ms. Same idea as the solution above, but better implementation."""
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res, cur, seen = 0, 0, {0}
        for i, n in enumerate(nums):
            cur += n
            prev = cur - target
            if prev in seen:
                res += 1
                seen = set()
            seen.add(cur)
        return res


class ACSolution:
    """O(n). 756ms. DP."""
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res, cur, dic = 0, 0, {0:0}
        for v in nums:
            cur += v
            res = max(res, dic.get(cur-target, -1) + 1)
            dic[cur] = res
        return res
