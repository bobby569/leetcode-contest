"""
https://leetcode.com/contest/biweekly-contest-32/problems/find-longest-awesome-substring/
"""


class ACSolution:
    """O(n) time. O(1024) space. 1752ms."""
    def longestAwesome(self, s: str) -> int:
        res, cur, n = 0, 0, len(s)
        seen = {0:-1}
        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen.get(cur ^ (1 << a), n))  # any number as middle char
            res = max(res, i - seen.get(cur, n))  # no middle char
            seen[cur] = min(seen.get(cur, n), i)
        return res


class OnceACSolution:
    """O(n^2) time. O(n) space. Got TLE on #152/153."""
    def longestAwesome(self, s: str) -> int:
        def count(s):
            res = 0
            while s:
                res += 1
                s &= s - 1
            return res

        acc = [0]
        for c in s:
            acc.append(acc[-1] ^ (1 << int(c)))
        res = 0
        for dlt in range(len(s), 0, -1):
            for i in range(len(s)-dlt+1):
                if count(acc[i] ^ acc[i+dlt]) <= 1:
                    return dlt
