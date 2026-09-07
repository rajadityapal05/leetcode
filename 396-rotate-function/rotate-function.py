class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)

        total = sum(nums)

        current = 0

        # Calculate F(0)
        for i in range(n):
            current += i * nums[i]

        answer = current

        # Calculate F(1), F(2), ..., F(n-1)
        for k in range(1, n):

            current = current + total - n * nums[n - k]

            answer = max(answer, current)

        return answer