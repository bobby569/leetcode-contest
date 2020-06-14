"""
https://leetcode.com/contest/biweekly-contest-28/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
"""
import bisect, collections, itertools, math


class MySolution:
    """Got TLE on #50/57."""
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def findLength(arr):
            s = collections.defaultdict(list)
            for i, n in enumerate(arr):
                s[n].append(i)
            res = float('inf')
            for i, n in enumerate(arr):
                if n - target in s:
                    idx = bisect.bisect_right(s[n-target], i) - 1
                    res = min(res, i - s[n-target][idx])
            return -1 if res == float('inf') else res

        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] + n)
        print(prefix)
        res = float('inf')
        for i in range(1, len(prefix)-1):
            first = findLength(prefix[:i+1])
            if first == -1:
                continue
            second = findLength(prefix[i:])
            if second == -1:
                break
            res = min(res, first + second)
            print(i, first, second)
        return -1 if res == float('inf') else res


class ACSolution:
    """DP. O(n). 984ms."""
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for idx, cur in enumerate(itertools.accumulate(arr)):
            end = prefix.get(cur - target)
            if end is not None:
                if end > -1:
                    ans = min(ans, idx - end + best_till[end])
                best = min(best, idx - end)
            best_till[idx] = best  # dp step to record the min length before idx
            prefix[cur] = idx  # update the latest index with the accumulate sum
        return -1 if ans == math.inf else ans
