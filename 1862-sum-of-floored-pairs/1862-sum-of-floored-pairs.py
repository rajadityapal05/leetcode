class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        freq = [0] * (max_num + 1)

        for x in nums:
            freq[x] += 1

        prefix = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + freq[i]

        ans = 0

        for y in range(1, max_num + 1):
            if freq[y] == 0:
                continue

            for multiple in range(y, max_num + 1, y):
                quotient = multiple // y
                right = min(multiple + y - 1, max_num)
                count = prefix[right] - prefix[multiple - 1]
                ans = (ans + freq[y] * quotient * count) % MOD

        return ans