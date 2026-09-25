class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        # Check whether a + b is a perfect square
        def is_square(x):
            r = isqrt(x)
            return r * r == x

        # adjacency[i][j] = whether nums[i] + nums[j] is square
        adjacency = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if is_square(nums[i] + nums[j]):
                    adjacency[i][j] = True
                    adjacency[j][i] = True

        @cache
        def dp(mask, last):
            # All numbers have been used
            if mask == (1 << n) - 1:
                return 1

            ans = 0

            for i in range(n):
                # Already used
                if mask & (1 << i):
                    continue

                # Current number cannot follow last
                if last != n and not adjacency[last][i]:
                    continue

                # Skip duplicate values at the same level
                if i > 0 and nums[i] == nums[i - 1] \
                        and not (mask & (1 << (i - 1))):
                    continue

                ans += dp(mask | (1 << i), i)

            return ans

        return dp(0, n)