class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = -1
        right = -1

        max_so_far = float('-inf')
        min_so_far = float('inf')

        # Find the right boundary
        for i in range(n):
            if nums[i] < max_so_far:
                right = i
            else:
                max_so_far = nums[i]

        # Find the left boundary
        for i in range(n - 1, -1, -1):
            if nums[i] > min_so_far:
                left = i
            else:
                min_so_far = nums[i]

        return 0 if right == -1 else right - left + 1