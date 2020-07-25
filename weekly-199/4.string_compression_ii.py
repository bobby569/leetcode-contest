"""
https://leetcode.com/contest/weekly-contest-199/problems/string-compression-ii/
"""
import functools
import math


class ACSolution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def helper(start, last, last_count, left):
            if left < 0:
                return math.inf
            if start >= len(s):
                return 0
            if s[start] == last:
                incr = 1 if last_count in (1, 9, 99) else 0
                # no need to delete
                return incr + helper(start+1, last, last_count+1, left)

            keep = 1 + helper(start+1, s[start], 1, left)
            delete = helper(start+1, last, last_count, left-1)
            return min(keep, delete)

        return helper(0, '', 0, k)
