class Solution:
    def maxValueAfterReverse(self, nums):
        n = len(nums)

        # Original value
        total = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))

        gain = 0

        # Reversal touching the left or right boundary
        for i in range(1, n):
            gain = max(
                gain,
                abs(nums[0] - nums[i]) - abs(nums[i - 1] - nums[i]),
                abs(nums[-1] - nums[i - 1]) - abs(nums[i - 1] - nums[i])
            )

        # Internal reversal
        # For edges (a,b) and (c,d), the new edges are (a,c) and (b,d).
        max_low = -10**18
        min_high = 10**18

        for i in range(n - 1):
            a = nums[i]
            b = nums[i + 1]

            low = min(a, b)
            high = max(a, b)

            max_low = max(max_low, low)
            min_high = min(min_high, high)

            gain = max(gain, 2 * (max_low - min_high))

        return total + gain