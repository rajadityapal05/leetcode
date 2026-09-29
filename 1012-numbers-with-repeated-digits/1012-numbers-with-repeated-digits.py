class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n)))
        m = len(digits)

        # Count positive numbers with unique digits
        unique = 0

        # Numbers with fewer digits than n
        for length in range(1, m):
            # First digit: 1-9 -> 9 choices
            # Remaining digits: choose from unused digits
            count = 9
            for i in range(1, length):
                count *= 10 - i
            unique += count

        # Numbers with the same number of digits as n
        used = set()

        for i, digit in enumerate(digits):
            # Try putting a smaller digit at this position
            start = 1 if i == 0 else 0

            for d in range(start, digit):
                if d not in used:
                    # Remaining positions can use any unused digits
                    remaining = m - i - 1
                    choices = 10 - (i + 1)

                    count = 1
                    for j in range(remaining):
                        count *= choices - j

                    unique += count

            # If current digit is already used,
            # n itself cannot contribute to unique numbers.
            if digit in used:
                break

            used.add(digit)

        else:
            # n itself has all unique digits
            unique += 1

        return n - unique