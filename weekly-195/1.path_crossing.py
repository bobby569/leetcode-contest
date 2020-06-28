"""
https://leetcode.com/contest/weekly-contest-195/problems/path-crossing/
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y, res = 0, 0, {(0,0)}
        for c in path:
            if c == 'E': x += 1
            if c == 'W': x -= 1
            if c == 'S': y -= 1
            if c == 'N': y += 1
            if (x, y) in res:
                return True
            res.add((x, y))
        return False
