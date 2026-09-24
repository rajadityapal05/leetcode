class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = number of ways using current point
        # to have j segments where the last segment is open.
        dp = [0] * (k + 1)
        dp[0] = 1

        for _ in range(n):
            new = dp[:]

            for j in range(1, k + 1):
                new[j] = (new[j] + dp[j - 1]) % MOD

            dp = new

        # Equivalent closed-form DP:
        # C(n + k - 1, 2k)
        ans = 1

        for i in range(1, 2 * k + 1):
            ans = ans * (n + k - i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans