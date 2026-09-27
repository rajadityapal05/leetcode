from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If a common divisor string exists, the concatenations
        # must be equal in both orders.
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]