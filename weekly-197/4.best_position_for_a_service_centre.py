"""
https://leetcode.com/contest/weekly-contest-197/problems/best-position-for-a-service-centre/
"""


class Solution:
    """316ms."""
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dist(x0, y0):
            return sum(((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 for x, y in positions)

        n = len(positions)
        xs = sum(x for x, _ in positions) / n
        ys = sum(y for _, y in positions) / n

        d = dist(xs, ys)
        step, direction = 0.5, [(0,1),(0,-1),(1,0),(-1,0)]

        while step > 0.000001:
            done = False
            for dx, dy in direction:
                tx = xs + step * dx
                ty = ys + step * dy
                t = dist(tx, ty)
                if t < d:
                    d, xs, ys, done = t, tx, ty, True
                    break
            if not done:
                step *= 0.7  # randomly chose 0.7 as the rate
        return d
