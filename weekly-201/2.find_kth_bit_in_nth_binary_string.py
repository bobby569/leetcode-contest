"""
https://leetcode.com/contest/weekly-contest-201/problems/find-kth-bit-in-nth-binary-string/
"""


class Solution:
    """Brute force. AC'd."""
    def findKthBit(self, n: int, k: int) -> str:
        t = "011100110110001"
        if n <= 4:
            return t[k-1]
        for _ in range(n-4):
            t = t + '1' + ''.join('1' if c == '0' else '0' for c in t[::-1])
        return t[k-1]


class Solution:
    """Use recursion."""
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        l = 2 ** n - 1  # length of S_n
        mid = (l >> 2) + 1
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, l - k + 1) == '0' else '0'
