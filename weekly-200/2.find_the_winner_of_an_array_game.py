"""
https://leetcode.com/contest/weekly-contest-200/problems/find-the-winner-of-an-array-game/
"""


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # if k is larger than or equal to the length of arr
        # the maximum of arr must be the answer
        if k >= len(arr):
            return max(arr)

        # do what is described and record the number of win
        winner, win = arr.pop(0), 0
        while True:
            tmp = arr.pop(0)
            if tmp > winner:
                arr.append(winner)
                winner, win = tmp, 1
            else:
                arr.append(tmp)
                win += 1
            if win == k:
                return winner
