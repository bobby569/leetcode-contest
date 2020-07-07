"""
https://leetcode.com/contest/weekly-contest-196/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left and not right:
            return 0
        if not left:
            return n - min(right)
        if not right:
            return max(left)
        return max(max(left), n-min(right))

        # one-liner
        return max(max(left, default=0), n - min(right, default=n))
