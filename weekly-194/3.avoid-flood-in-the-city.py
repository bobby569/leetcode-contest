"""
https://leetcode.com/contest/weekly-contest-194/problems/avoid-flood-in-the-city/
"""
import bisect


class Solution:
    """O(nlogn). 1348ms."""
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_on_day, drain_days, res = {}, [], rains[:]
        for i, r in enumerate(rains):
            if r == 0:
                if len(full_on_day) != 0:
                    drain_days.append(i)
            else:
                if r in full_on_day:
                    idx = bisect.bisect_right(drain_days, full_on_day[r])
                    if idx == len(drain_days):
                        return []
                    day = drain_days[idx]
                    del drain_days[idx]
                    res[day] = r  # on day drain r
                full_on_day[r] = i

        for i, r in enumerate(rains):
            res[i] = max(1, res[i]) if r == 0 else -1
        return res
