"""
https://leetcode.com/contest/weekly-contest-199/problems/number-of-good-leaf-nodes-pairs/
"""
import bisect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, dist: int) -> int:
        def helper(node):
            nonlocal res
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = helper(node.left)
            right = helper(node.right)
            if left and right:
                tmp = sorted(l + r for l in left for r in right)
                res += bisect.bisect_right(tmp, dist)
            return [n+1 for n in sorted(left + right)]

        res = 0
        helper(root)
        return res
