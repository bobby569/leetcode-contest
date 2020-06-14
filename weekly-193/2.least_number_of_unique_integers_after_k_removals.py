"""
https://leetcode.com/contest/weekly-contest-193/problems/least-number-of-unique-integers-after-k-removals/
"""
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        lst = sorted(collections.Counter(arr).values())
        while lst and lst[0] <= k:
            k -= lst[0]
            lst.pop(0)
        return len(lst)
