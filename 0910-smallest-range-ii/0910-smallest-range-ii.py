class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        if n == 1:
            return 0

        # Initially, don't change anything.
        answer = nums[-1] - nums[0]

        for i in range(n - 1):
            # Left side gets +k
            high = max(nums[i] + k, nums[-1] - k)

            # Right side gets -k
            low = min(nums[0] + k, nums[i + 1] - k)

            answer = min(answer, high - low)

        return answer