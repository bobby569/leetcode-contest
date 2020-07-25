"""
https://leetcode.com/contest/biweekly-contest-31/problems/number-of-good-ways-to-split-a-string/
"""
import collections


class Solution:
    def numSplits(self, s: str) -> int:
        c1, c2 = collections.Counter(s[0]), collections.Counter(s[1:])
        res = int(len(c2) == 1)
        for c in s[1:-1]:
            c1[c] += 1
            c2[c] -= 1
            if c2[c] == 0:
                del c2[c]
            res += len(c1) == len(c2)
        return res
