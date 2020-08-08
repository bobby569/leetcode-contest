"""
https://leetcode.com/contest/weekly-contest-201/problems/make-the-string-great/
"""


class Solution:
    def makeGood(self, s: str) -> str:
        s, changed = list(s), True
        while changed:
            i, changed = 0, False
            while i < len(s)-1:
                if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    changed = True
                    continue
                i += 1
        return ''.join(s)


# or use stack
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2 and abs(ord(stack[-2]) - ord(stack[-1])) == 32:
                stack.pop()
                stack.pop()
        return ''.join(stack)
