"""
https://leetcode.com/contest/biweekly-contest-28/problems/final-prices-with-a-special-discount-in-a-shop/
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, p in enumerate(prices):
            for np in prices[i+1:]:
                if np <= p:
                    prices[i] -= np
                    break
        return prices
