class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0

        for i in range(n):
            count = 0

            while nums[i] != -1:
                next_index = nums[i]
                nums[i] = -1
                i = next_index
                count += 1

            max_length = max(max_length, count)

        return max_length