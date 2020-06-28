"""
https://leetcode.com/contest/weekly-contest-195/problems/max-value-of-equation/
"""
import collections
import math
import heapq


class MySolution:
    """O(nk). Got TLE on #64/65."""
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue, res = collections.deque(), -math.inf
        for x, y in points:
            while queue and x - queue[0][0] > k:
                queue.popleft()
            for x0, y0 in queue:  # one step away from ACSolution2
                res = max(res, y + y0 + x - x0)
            while queue and y - x >= queue[-1][1] - queue[-1][0]:
                queue.pop()
            queue.append((x, y))
        return res


class ACSolution1:
    """O(nlogn). Use Priority Queue."""
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue, res = [], -math.inf
        for x, y in points:
            while queue and queue[0][1] < x-k:
                heapq.heappop(queue)
            if queue:
                res = max(res, -queue[0][0] + x + y)
            heapq.heappush(queue, (x-y, x))
        return res


class ACSolution2:
    """O(n). Use Stack."""
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue, res = collections.deque(), -math.inf
        for x, y in points:
            while queue and queue[0][1] < x - k:
                queue.popleft()
            if queue:
                res = max(res, queue[0][0] + x + y)
            while queue and queue[-1][0] <= y - x:
                queue.pop()
            queue.append((y-x, x))
        return res
