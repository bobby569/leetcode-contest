"""
https://leetcode.com/contest/weekly-contest-196/problems/count-submatrices-with-all-ones/
"""


class ACSolution1:
    """O(nnm). 1112ms."""
    def numSubmat(self, mat: List[List[int]]) -> int:
        def countOneRow(arr: list) -> int:
            res = cur = 0
            for v in arr:
                cur = cur + 1 if v else 0
                res += cur
            return res

        res, n, m = 0, len(mat), len(mat[0])
        for up in range(n):
            h = [1] * m
            for down in range(up, n):
                for k in range(m):
                    h[k] &= mat[down][k]
                tmp = countOneRow(h)
                if tmp == 0:
                    break
                res += tmp
        return res


class ACSolution2:
    """O(nm). Stack."""
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(mat):
            for j in range(len(mat[0])):
                if i and row[j]:
                    row[j] += mat[i-1][j]
            stack, sub = [-1], 0
            for j, h in enumerate(row):
                while stack[-1] >= 0 and row[stack[-1]] >= h:
                    j0 = stack.pop()
                    sub -= row[j0] * (j0 - stack[-1])
                sub += h * (j - stack[-1])
                res += sub
                stack.append(j)
        return res
