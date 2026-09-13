class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # dp[k] = set of sums achievable using exactly k elements
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n - 1, -1, -1):
                for s in dp[k]:
                    dp[k + 1].add(s + num)

        # Check whether a valid subset exists
        for k in range(1, n):
            if total * k % n == 0:
                target = total * k // n

                if target in dp[k]:
                    return True

        return False