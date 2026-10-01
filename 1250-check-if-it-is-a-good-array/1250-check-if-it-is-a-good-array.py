from math import gcd

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        g = 0

        for num in nums:
            g = gcd(g, num)

            if g == 1:
                return True

        return False