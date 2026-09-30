class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Remove all factors of 2
        while n % 2 == 0:
            n //= 2

        # Count divisors of the remaining odd number
        count = 1
        factor = 3

        while factor * factor <= n:
            if n % factor == 0:
                exponent = 0

                while n % factor == 0:
                    n //= factor
                    exponent += 1

                count *= exponent + 1

            factor += 2

        # If n has a prime factor greater than sqrt(original n)
        if n > 1:
            count *= 2

        return count