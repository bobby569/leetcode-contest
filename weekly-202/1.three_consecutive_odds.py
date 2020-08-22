"""
https://leetcode.com/contest/weekly-contest-202/problems/three-consecutive-odds/
"""


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for n in arr:
            if n & 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
