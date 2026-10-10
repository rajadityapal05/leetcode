
from functools import lru_cache
from math import gcd

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        m = len(nums)

        @lru_cache(None)
        def dp(mask):
            if mask == (1 << m) - 1:
                return 0

            operation = mask.bit_count() // 2 + 1
            best = 0

            for i in range(m):
                if mask & (1 << i):
                    continue

                for j in range(i + 1, m):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << i) | (1 << j)
                    score = operation * gcd(nums[i], nums[j])
                    best = max(best, score + dp(new_mask))

            return best

        return dp(0)
 