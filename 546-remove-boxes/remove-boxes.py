from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            # Merge consecutive boxes of the same color
            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            # Option 1: Remove the current group immediately
            ans = (k + 1) ** 2 + dp(l + 1, r, 0)

            # Option 2: Merge with a later group of the same color
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    ans = max(
                        ans,
                        dp(l + 1, i - 1, 0) + dp(i, r, k + 1)
                    )

            return ans

        return dp(0, len(boxes) - 1, 0) 