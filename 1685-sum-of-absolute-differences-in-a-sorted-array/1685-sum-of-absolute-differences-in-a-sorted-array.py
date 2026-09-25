class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)

        result = []
        prefix = 0

        for i, x in enumerate(nums):
            # Elements to the left
            left = x * i - prefix

            # Elements to the right
            right = (total - prefix - x) - x * (n - i - 1)

            result.append(left + right)

            prefix += x

        return result