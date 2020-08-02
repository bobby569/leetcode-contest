"""
https://leetcode.com/contest/weekly-contest-200/problems/get-the-maximum-score/
"""


class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        MOD = 1000000007
        common = set(A) & set(B)

        res = i = j = 0
        while i < len(A) and j < len(B):
            tmpA = 0
            while i < len(A) and A[i] not in common:
                tmpA += A[i]
                i += 1
            tmpB = 0
            while j < len(B) and B[j] not in common:
                tmpB += B[j]
                j += 1
            res += max(tmpA, tmpB)
            i += 1
            j += 1

        res += max(sum(A[i:]), sum(B[j:])) + sum(common)  # add the rest
        return res % MOD
