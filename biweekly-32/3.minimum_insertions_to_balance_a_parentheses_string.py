"""
https://leetcode.com/contest/biweekly-contest-32/problems/minimum-insertions-to-balance-a-parentheses-string/
"""
from typing import List, Tuple


class ACSolution:
    """O(n). 196ms. Use stack."""
    def minInsertions(self, s: str) -> int:
        stack, res = [], 0
        for c in s:
            if not stack:
                if c == ')':
                    res += 1
                    stack.append('(')  # insert a '(' for ')'
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.append(c)
                else:  # stack[-1] == ')'
                    stack.pop()
                    if c == '(':
                        res += 1  # insert a ')' to have a match
                    else:
                        stack.pop()  # has a match
        while stack:
            last = stack.pop()
            if last == '(':
                res += 2
            else:
                stack.pop()
                res += 1
        return res


class ACSolution:
    """O(n). 180ms. Use counter."""
    def minInsertions(self, s: str) -> int:
        res = right = 0
        for c in s:
            if c == '(':
                right += 2
                if right & 1:  # have odd ')' before
                    right -= 1
                    res += 1
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return res + right
