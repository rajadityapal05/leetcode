class Solution:
    def soupServings(self, n: int) -> float:
        from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        n = (n + 24) // 25

        @lru_cache(None)
        def dp(a, b):
            # Both finish together
            if a <= 0 and b <= 0:
                return 0.5

            # A finishes first
            if a <= 0:
                return 1.0

            # B finishes first
            if b <= 0:
                return 0.0

            return (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            ) / 4

        return dp(n, n)