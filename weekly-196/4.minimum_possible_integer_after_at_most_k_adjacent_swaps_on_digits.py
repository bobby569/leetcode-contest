"""
https://leetcode.com/contest/weekly-contest-196/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
"""
import collections
import string
from sortedcontainers import SortedList

class ACSolution1:
    """O(n^2). Should have TLE but passed."""
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n * (n-1) / 2:
            return ''.join(sorted(num))
        res, q = [], [(v, i) for i, v in enumerate(num)]
        while k and q:
            idx, (v, i) = min(enumerate(q[:k+1]), key=lambda p: p[1])
            k -= idx
            del q[idx]
            res += v
        res += [v for v, _ in q]
        return ''.join(res)


class ACSolution2:
    """O(n^2). Should have TLE but passed."""
    def minInteger(self, num: str, k: int) -> str:
        # base case
        if k <= 0:
            return num
        n = len(num)
        if k >= n * (n-1) / 2:
            return ''.join(sorted(num))

        # starting from the smallest number
        for i in range(10):
            # find the smallest index
            idx = num.find(str(i))
            # if this index is valid
            if 0 <= idx <= k:
                # move the digit to the front and deal with the rest of the string recursively.
                return num[idx] + self.minInteger(num[0:idx] + num[idx+1:], k-idx)


class Solution:
    """O(nlogn)."""
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n * (n-1) / 2:
            return ''.join(sorted(num))

        d = collections.defaultdict(collections.deque)
        for i, v in enumerate(num):
            d[v].append(i)

        ans, seen = '', SortedList()
        for _ in range(len(num)):
            for a in string.digits:
                if d[a]:
                    idx = d[a][0]
                    ni = idx + (len(seen) - seen.bisect(idx))
                    dist = ni - len(seen)
                    if dist <= k:
                        k -= dist
                        d[a].popleft()
                        ans += a
                        seen.add(idx)
                        break
        return ans
