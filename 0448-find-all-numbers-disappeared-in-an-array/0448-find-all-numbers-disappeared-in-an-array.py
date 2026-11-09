class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Mark numbers that are present
        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        # Collect missing numbers
        result = []

        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result 