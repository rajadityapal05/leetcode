class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))

        # Store the last position of each digit
        last = {}

        for i, digit in enumerate(digits):
            last[digit] = i

        # Try to improve each digit from left to right
        for i in range(len(digits)):
            for d in range(9, int(digits[i]), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]

                    digits[i], digits[j] = digits[j], digits[i]

                    return int("".join(digits))

        return num