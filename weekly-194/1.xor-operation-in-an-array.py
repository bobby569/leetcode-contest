"""
https://leetcode.com/contest/weekly-contest-194/problems/xor-operation-in-an-array/
"""
import functools


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]

        # normal way
        res = 0
        for n in arr:
            res ^= n
        return res

        # one-liner, use reduce
        return functools.reduce(lambda x, y: x ^ y, arr, 0)
