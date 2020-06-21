"""
https://leetcode.com/contest/weekly-contest-194/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
"""
import collections
import math


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, a):
        if self.par[a] == a:
            return a
        return self.find(self.par[a])

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if a > b:
            a, b = b, a
        self.par[b] = a
        return True


class ACSolution:
    """Union Find. 2132ms."""
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        E = sorted((w, s, d, i) for i, (s, d, w) in enumerate(edges))

        def find_mst_without_edge(e):
            uf = UnionFind(n)
            res = 0
            for i, (w, s, d, _) in enumerate(E):
                if i != e and uf.union(s, d):
                    res += w
            return res if all(uf.find(i) == 0 for i in range(n)) else -math.inf

        def find_mst_with_edge(e):
            uf = UnionFind(n)
            res = E[e][0]
            uf.union(E[e][1], E[e][2])
            for i, (w, s, d, _) in enumerate(E):
                if i != e and uf.union(s, d):
                    res += w
            return res if all(uf.find(i) == 0 for i in range(n)) else -math.inf

        base = find_mst_without_edge(-1)
        critical, pseudo_critical = set(), set()
        for i, e in enumerate(E):
            v = find_mst_without_edge(i)
            if v != base:  # If MST value increases, every mst use this edge.
                critical.add(e[3])
            else:
                v = find_mst_with_edge(i)
                if v == base:   # If MST value remains, at least one mst using this edge exists
                    pseudo_critical.add(e[3])
        return [list(critical), list(pseudo_critical)]


class ACSolution:
    """DFS. 316ms."""
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def ok(u, tu, tv, tw, visited):
            if u == tv:
                return True
            if visited[u]:
                return False
            visited[u] = True

            for v, w in graph[u].items():
                if (u, v) == (tu, tv):  # skip the current edge
                    continue
                if w <= tw and ok(v, tu, tv, tw, visited):
                    return True
            return False


        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        critical, pseudo_critical = [], []
        for i, (u, v, w) in enumerate(edges):
            # check if this edge is in any mst
            # if mst exists with largest weight to be w-1
            # then this edge must not exist in any mst
            if ok(u, u, v, w-1, [False] * n):
                continue
            if ok(u, u, v, w, [False] * n):
                pseudo_critical.append(i)
            else:
                critical.append(i)
        return [critical, pseudo_critical]
