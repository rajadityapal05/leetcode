class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for length in range(1, goal + 1):
            for used in range(1, min(length, n) + 1):

                # Add a new song
                dp[length][used] += (
                    dp[length - 1][used - 1] * (n - used + 1)
                )

                # Replay an old song
                if used > k:
                    dp[length][used] += (
                        dp[length - 1][used] * (used - k)
                    )

                dp[length][used] %= MOD

        return dp[goal][n]