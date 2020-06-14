"""
https://leetcode.com/contest/weekly-contest-193/problems/minimum-number-of-days-to-make-m-bouquets/
"""


class MySolution:
    """Got TLE on #87/91."""
    def minDays(self, bDs: List[int], m: int, k: int) -> int:
        total = m * k
        if total > len(bDs): return -1

        def check(day: int) -> bool:
            arr = [1 if n <= day else 0 for n in bDs]
            if sum(arr) < total: return False

            i, left = 0, m
            while i + k <= len(arr):
                if arr[i] and all(arr[i:i+k]):
                    left -= 1
                    if left == 0:
                        return True
                    i += k
                else:
                    i += 1
            return False

        lo, hi = min(bDs), max(bDs)
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi): hi = mi
            else: lo = mi + 1
        return hi


class ACSolution:
    """O(n(lgn)^2 + 2nlgn). 5140ms."""
    def minDays(self, bDs: List[int], m: int, k: int) -> int:
        def possible(days: int) -> bool:
            flowers = []
            for d, i in events:
                if d > days: break
                flowers.append(i)
            flowers.sort()

            bouquets = left = 0
            for right, x in enumerate(flowers):
                if right == len(flowers) - 1 or flowers[right + 1] != x + 1:
                    bouquets += (right - left + 1) // k
                    left = right + 1
            return bouquets >= m

        events = sorted((d, i) for i, d in enumerate(bDs))
        lo, hi = 0, len(events)  # set `high` to the length of the list for existence check
        while lo < hi:
            mi = lo + hi >> 1
            if possible(events[mi][0]): hi = mi
            else: lo = mi + 1
        return events[lo][0] if lo < len(events) else -1


class ACSolution2:
    """O(nlgn). 1356ms."""
    def minDays(self, bDs: List[int], m: int, k: int) -> int:
        def possible(days):
            num_in_seg = bouquets = 0
            for i in bDs:
                if i <= days:
                    num_in_seg += 1
                else:
                    bouquets += num_in_seg // k
                    num_in_seg = 0
            bouquets += num_in_seg // k
            return bouquets >= m

        if m * k > len(bDs): return -1
        lo, hi = min(bDs), max(bDs)
        while lo < hi:
            mi = (lo + hi) >> 1
            if possible(mi): hi = mi
            else: lo = mi + 1
        return hi
