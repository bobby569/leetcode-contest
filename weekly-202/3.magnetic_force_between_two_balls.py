"""
https://leetcode.com/contest/weekly-contest-202/problems/magnetic-force-between-two-balls/
"""
import bisect


class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        def is_possible(force):
            t, idx = m-1, 0
            while t > 0 and idx < len(pos):
                idx = bisect.bisect_left(pos, pos[idx] + force)
                t -= 1
            return t == 0 and idx < len(pos)

        pos.sort()
        lo, hi = 1, pos[-1]
        while lo < hi:
            mi = (lo + hi) >> 1
            if is_possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
