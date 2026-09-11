class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))

        mark = len(digits)

        # Find where monotone increasing property breaks
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                mark = i

        # Make all digits after the changed position 9
        for i in range(mark, len(digits)):
            digits[i] = '9'

        return int(''.join(digits))