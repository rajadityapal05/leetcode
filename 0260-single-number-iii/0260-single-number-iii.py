class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0

        # Step 1: XOR all numbers
        for num in nums:
            xor ^= num

        # Step 2: Find a bit where the two numbers differ
        bit = xor & -xor

        # Step 3: Separate numbers into two groups
        a = 0
        b = 0

        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        return [a, b]