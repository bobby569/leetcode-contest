"""
https://leetcode.com/contest/biweekly-contest-30/problems/reformat-date/
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        return '%s-%02d-%02d' % (year, int(M.index(month) + 1), int(day[:-2]))
