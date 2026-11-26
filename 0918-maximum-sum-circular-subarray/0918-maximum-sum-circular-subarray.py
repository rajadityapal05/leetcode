
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_sum = float('-inf')
        min_sum = float('inf')

        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
