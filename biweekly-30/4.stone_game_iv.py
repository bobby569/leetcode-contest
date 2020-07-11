"""
https://leetcode.com/contest/biweekly-contest-30/problems/stone-game-iv/
"""
import math


class MySolution:
    """Fail 66/72. Maximum recursion depth exceeded for input n=31250."""
    def winnerSquareGame(self, n: int) -> bool:
        win = {1,3,4,6,8,9,11,13}
        lose = {2,5,7,10,12}

        @functools.lru_cache(None)
        def dfs(who, left):
            if left < 14:
                return (who == 'A' and left in win) or (who == 'B' and left in lose)
            sq = int(math.sqrt(left))
            if sq ** 2 == left:
                return who == 'A'
            if who == 'B':
                return all(dfs('A', left - chosen ** 2) for chosen in range(1, sq+1))
            if who == 'A':
                return any(dfs('B', left - chosen ** 2) for chosen in range(1, sq+1))

        return dfs('A', n)


class MySolution2:
    """O(n^1.5). 3980ms."""
    def winnerSquareGame(self, n: int) -> bool:
        win = {0,1,3,4,6,8,9,11,13,14,16}
        if n < 17:
            return n in win
        dp = [None] * (n+1)
        for i in range(1, 17):
            dp[i] = i in win

        sq = int(math.sqrt(n))
        if sq ** 2 == n:
            return True
        for i in range(5, sq+1):
            dp[i**2] = True

        for i in range(17, n+1):
            if dp[i] is None:
                sq = int(math.sqrt(i))
                dp[i] = any(not dp[i - k ** 2] for k in range(1, sq+1))
        return dp[-1]


class ACSolution1:
    """O(n^1.5). 4396ms."""
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k ** 2] for k in range(1, int(i**0.5) + 1))
        return dp[-1]


class ACSolution2:
    """O(n). 272ms."""
    def winnerSquareGame(self, n: int) -> bool:
        sqs = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [False] * (n+1)
        for i in range(n+1):
            if dp[i]:
                continue  # winning, any dp[i+sqs] is False
            for sq in sqs:
                if i + sq > n:
                    break
                dp[i + sq] = True
        return dp[n]
