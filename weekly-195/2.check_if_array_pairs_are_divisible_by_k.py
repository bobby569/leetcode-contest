"""
https://leetcode.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/
"""


class Solution:
    def canArrange(self, arr: List[int], K: int) -> bool:
        dic = {}
        for n in arr:
            r = n % K
            dic[r] = dic.get(r, 0) + 1
        if dic.get(0):
            if dic[0] & 1:
                return False
            del dic[0]
        for k, v in dic.items():
            if v != dic.get(K-k, 0):
                return False
        return True
