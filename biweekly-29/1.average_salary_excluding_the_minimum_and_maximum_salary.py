"""
https://leetcode.com/contest/biweekly_contest_29/problems/average_salary_excluding_the_minimum_and_maximum_salary/
"""


class Solution:
    def average(self, S: List[int]) -> float:
        return (sum(S) - min(S) - max(S)) / (len(S) - 2)
