
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0.0] * n

        for i in range(n):
            dp[i] = prefix[i + 1] / (i + 1)

        for groups in range(2, k + 1):
            for i in range(n - 1, groups - 2, -1):
                for j in range(groups - 2, i):
                    avg = (prefix[i + 1] - prefix[j + 1]) / (i - j)
                    dp[i] = max(dp[i], dp[j] + avg)

        return dp[n - 1]
