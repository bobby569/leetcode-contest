"""
https://leetcode.com/contest/biweekly-contest-31/problems/number-of-sub-arrays-with-odd-sum/
"""


class MySolution:
    """O(n^2). Got TLE #116/151."""
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i, v in enumerate(arr):
            tmp = v & 1
            res += tmp
            for n in arr[i+1:]:
                tmp ^= n & 1
                res += tmp
        return res % 10000000007


class ACSolution:
    """O(n). 1328ms."""
    def numOfSubarrays(self, arr: List[int]) -> int:
        cnt, cur, res = [1, 0], 0, 0
        for n in arr:
            cur = (cur + n) & 1
            res += cnt[cur^1]
            cnt[cur] += 1
        return res % 1000000007
