class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        digits = "0123456789abcdef"

        num &= 0xFFFFFFFF

        result = ""

        while num > 0:
            remainder = num & 15
            result = digits[remainder] + result
            num >>= 4

        return result