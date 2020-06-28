"""
https://leetcode.com/contest/biweekly-contest-29/problems/parallel-courses-ii/
"""
import collections
import itertools


class MySolution1:
    """Failed on #51/53 with n=8, D=[[1,6],[2,7],[8,7],[2,5],[3,4]], k=3."""
    def minNumberOfSemesters(self, n: int, D: List[List[int]], k: int) -> int:
        graph = collections.defaultdict(set)
        for s, d in D:
            graph[s]
            graph[d].add(s)
        indep = list(set(range(1, n+1)) - set(graph))

        res = 0
        while graph or indep:
            res += 1
            zero = [n for n, s in graph.items() if len(s) == 0][:k]
            s = set(zero)
            for v in s:
                del graph[v]
            for n in graph:
                graph[n] -= s
            if len(zero) < k and indep:
                t = k-len(zero)
                zero += indep[:t]
                indep = indep[t:]
        return res


class MySolution2:
    """32ms. But greedy is wrong."""
    def minNumberOfSemesters(self, n: int, D: List[List[int]], k: int) -> int:
        graph = {i: [set(), set()] for i in range(1, n+1)}  # node: [in_nodes, out_nodes]
        for s, d in D:
            graph[s][1].add(d)
            graph[d][0].add(s)

        res = 0
        queue = [(i, len(outd)) for i, (ind, outd) in graph.items() if not ind]
        while queue:
            res += 1
            queue.sort(key=lambda x: -x[1])
            taken, queue = queue[:k], queue[k:]
            for take, _ in taken:
                for out_node in graph[take][1]:
                    graph[out_node][0].remove(take)
                    if not graph[out_node][0]:
                        queue.append((out_node, len(graph[out_node][1])))
        return res


class ACSolution:
    """O(n^2*2^n). Actually working solution."""
    def minNumberOfSemesters(self, n, dependencies, k):
        dp = [[(0, 100)] * n for _ in range(1 << n)]

        bm_dep = [0] * n
        for i,j in dependencies:
            bm_dep[j-1]^=(1<<(i-1))

        for i in range(n):
            if bm_dep[i] == 0:
                dp[1 << i][i] = (1 << i, 1)

        for i in range(1 << n):
            n_z_bits = [len(bin(i)) - p - 1 for p,c in enumerate(bin(i)) if c == "1"]

            for t, j in itertools.permutations(n_z_bits, 2):
                if bm_dep[j] & i == bm_dep[j]:
                    mask, cand = dp[i ^ (1 << j)][t]
                    if bm_dep[j] & mask == 0 and bin(mask).count('1') < k:
                        if dp[i][j][1] > cand:
                            dp[i][j] =  (mask + (1 << j), cand)
                    else:
                        if dp[i][j][1] > cand + 1:
                            dp[i][j] = (1 << j, cand + 1)
        return min(j for _, j in dp[-1])
