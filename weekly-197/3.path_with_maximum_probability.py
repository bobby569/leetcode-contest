"""
https://leetcode.com/contest/weekly-contest-197/problems/path-with-maximum-probability/
"""
import collections
import heapq


class Solution:
    """1260ms."""
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for (f, t), p in zip(edges, succProb):
            graph[f][t] = p
            graph[t][f] = p

        value = [0] * n
        value[start] = 1

        deque = collections.deque([start])
        while deque:
            node = deque.popleft()
            for _next, _prob in graph[node].items():
                tmp = value[node] * _prob
                if tmp > value[_next]:
                    value[_next] = tmp
                    deque.append(_next)
        return value[end]


class ACSolution:
    """744ms."""
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for (f, t), p in zip(edges, succProb):
            graph[f][t] = p
            graph[t][f] = p

        heap, visited = [(-1, start)], set()
        while heap:
            prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return -prob
            for n, p in graph[node].items():
                heapq.heappush(heap, (p * prob, n))
        return 0
