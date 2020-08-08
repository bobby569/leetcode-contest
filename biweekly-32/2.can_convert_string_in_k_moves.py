"""
https://leetcode.com/contest/biweekly-contest-32/problems/can-convert-string-in-k-moves/
"""


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for i in range(len(s)):
            d = (ord(t[i]) - ord(s[i])) % 26
            if d == 0:
                continue
            if cnt[d] * 26 + d > k:
                return False
            cnt[d] += 1
        return True
