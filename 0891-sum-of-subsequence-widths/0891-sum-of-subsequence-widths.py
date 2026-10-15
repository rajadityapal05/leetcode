class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0
        power = 1

        for i, x in enumerate(nums):
            ans = (ans + x * (power - pow(2, len(nums) - 1 - i, MOD))) % MOD
            power = (power * 2) % MOD

        return ans