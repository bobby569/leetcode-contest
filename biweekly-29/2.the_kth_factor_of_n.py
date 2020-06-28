"""
https://leetcode.com/contest/biweekly-contest-29/problems/the-kth-factor-of-n/
"""
import math


class MySolution:
    """44ms."""
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        i, lo, hi = 2, [1], [n]

        while i <= math.sqrt(n):
            q, r = divmod(n, i)
            if r == 0:
                lo.append(i)
                if i != q:
                    hi.append(q)
            if len(lo) == k:
                return lo[-1]
            i += 1
        k -= len(lo)
        return hi[-k] if k <= len(hi) else -1


class ACSolution:
    """24ms."""
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if not k:
                    return i
        return -1
