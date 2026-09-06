class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        n = len(nums)
        answer = 0

        for bit in range(30):

            ones = 0

            for num in nums:
                if num & (1 << bit):
                    ones += 1

            zeros = n - ones

            answer += ones * zeros

        return answer