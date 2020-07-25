"""
https://leetcode.com/contest/weekly-contest-199/problems/shuffle-string/
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, v in enumerate(indices):
            res[v] = s[i]
        return ''.join(res)
