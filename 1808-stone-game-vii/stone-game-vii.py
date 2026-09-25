class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i] = best score difference for the current interval
        # Initially, an interval with one stone gives 0 points.
        dp = [0] * n

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # Remove left stone
                left = total - stones[i] - dp[i + 1]

                # Remove right stone
                right = total - stones[j] - dp[i]

                dp[i] = max(left, right)

        return dp[0]