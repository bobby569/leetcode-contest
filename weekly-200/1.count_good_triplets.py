"""
https://leetcode.com/contest/weekly-contest-200/problems/count-good-triplets/
"""


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i, v1 in enumerate(arr):
            for j, v2 in enumerate(arr[i+1:], i+1):
                if abs(v1-v2) <= a:
                    for v3 in arr[j+1:]:
                        if abs(v2-v3) <= b and abs(v1-v3) <= c:
                            res += 1
        return res
