"""
https://leetcode.com/contest/weekly-contest-193/problems/kth-ancestor-of-a-tree-node/
"""
import collections


class MyTreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.anc = collections.defaultdict(list)
        for i, p in enumerate(parent):
            self.anc[i] = [i, p]
        # call self._helper1() or self._helper2()

    def _helper1(self, n):
        """Got MLE on #10/10 test case."""
        for i in range(n):
            p = self.anc[i][1]
            self.anc[i].extend(self.anc[p][1:])

    def _helper2(self, n):
        """Got TLE on #10/10 test case."""
        for i in range(n):
            p = self.anc[i][1]
            while p >= 0:
                p = self.anc[p][1]
                self.anc[i].append(p)

    def getKthAncestor(self, node: int, k: int) -> int:
        ans = self.anc[node]
        return ans[k] if k < len(ans) else -1


class ACTreeAncestor1:
    """Binary lifting. 1212ms. 53.3M."""
    def __init__(self, n: int, parent: List[int]):
        self.parents = [parent]
        for k in range(1, 16):
            self.parents.append([])
            for node in range(n):
                p = self.parents[k-1][node]
                if p != -1:
                    p = self.parents[k-1][p]
                self.parents[k].append(p)

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(16):
            if k & 1 and node != -1:
                node = self.parents[k][node]
            k >>= 1
        return node


class ACTreeAncestor2:
    """Another implementation using dictionary. 924ms. 88.5M."""
    def __init__(self, n: int, parent: List[int]):
        parent = dict(enumerate(parent))
        self.parents = [parent]
        for _ in range(15):
            tmp = {}
            for i in parent:
                if parent[i] in parent:
                    tmp[i] = parent[parent[i]]
            self.parents.append(tmp)
            parent = tmp

    def getKthAncestor(self, node: int, k: int) -> int:
        step = 15
        while k > 0 and node > -1:
            if k >= 1 << step:
                node = self.parents[step].get(node, -1)
                k -= 1 << step
            else:
                step -= 1
        return node
