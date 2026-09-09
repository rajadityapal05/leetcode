class Solution:
    def nextGreaterElement(self, n):
        digits = list(str(n))

        # 1. Find the first decreasing digit
        i = len(digits) - 2

        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # No greater permutation
        if i < 0:
            return -1

        # 2. Find the smallest digit greater than digits[i]
        j = len(digits) - 1

        while digits[j] <= digits[i]:
            j -= 1

        # 3. Swap
        digits[i], digits[j] = digits[j], digits[i]

        # 4. Reverse the remaining digits
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int("".join(digits))

        # 5. Check 32-bit integer limit
        if result > 2**31 - 1:
            return -1

        return result