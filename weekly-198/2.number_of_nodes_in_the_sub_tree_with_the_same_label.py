"""
https://leetcode.com/contest/weekly-contest-198/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""
import collections


class Node:
    def __init__(self, val, label):
        self.val = val
        self.label = label
        self.children = set()


class Solution:
    """4492ms. Mistakenly treated this as a tree problem. Should be a graph."""
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            c = collections.Counter()
            if not node or node.val in visited:
                return c
            visited.add(node.val)
            for child in node.children:
                c += dfs(child)
            c[node.label] += 1
            res[node.val] = c[node.label]
            return c

        nodes = [Node(i, c) for i, c in enumerate(labels)]
        for p, c in edges:
            nodes[p].children.add(nodes[c])
            nodes[c].children.add(nodes[p])

        res, visited = [0] * n, set()
        dfs(nodes[0])
        return res


class Solution:
    """5468ms. Use graph."""
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(u, p):
            c = collections.Counter()
            if u is None:
                return c
            for v in graph[u]:
                if v != p:
                    c += dfs(v, u)
            c[labels[u]] += 1
            res[u] = c[labels[u]]
            return c

        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        res = [0] * n
        dfs(0, -1)
        return res
