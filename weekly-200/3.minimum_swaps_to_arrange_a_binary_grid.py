"""
https://leetcode.com/contest/weekly-contest-200/problems/minimum-swaps-to-arrange-a-binary-grid/
"""


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # find the number of tailing zero of each row
        zero, n = [], len(grid)
        for row in grid:
            tmp = 0
            while row and row.pop() == 0:
                tmp += 1
            zero.append(tmp)

        # similar to insertion sort
        res = 0
        for i in range(n):
            # skip since satisfies
            if zero[i] >= n-i-1:
                continue
            # find the closest valid one
            for j in range(i+1, n):
                if zero[j] >= n-i-1:
                    break
            # check if zero[j] is valid
            if zero[j] < n-i-1:
                return -1
            # insert step, move [i:j] one index forward
            zero[i+1:j+1] = zero[i:j]
            # add number of moves
            res += j-i
        return res
