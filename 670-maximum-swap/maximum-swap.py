class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))

        # Store the last position of each digit
        last = [-1] * 10

        for i, d in enumerate(digits):
            last[int(d)] = i

        # Find the first digit we can make larger
        for i, d in enumerate(digits):
            current = int(d)

            # Try larger digits, from 9 down to current + 1
            for bigger in range(9, current, -1):
                if last[bigger] > i:
                    j = last[bigger]

                    digits[i], digits[j] = digits[j], digits[i]

                    return int("".join(digits))

        return num