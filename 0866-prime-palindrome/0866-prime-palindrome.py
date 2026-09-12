class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_prime(x):
            if x < 2:
                return False

            if x % 2 == 0:
                return x == 2

            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2

            return True

        # Small prime palindromes
        for x in [2, 3, 5, 7, 11]:
            if x >= n:
                return x

        digits = len(str(n))

        while True:
            # Generate odd-length palindromes
            half_len = (digits + 1) // 2

            start = 10 ** (half_len - 1)
            end = 10 ** half_len

            for prefix in range(start, end):
                s = str(prefix)

                # Mirror everything except the last digit
                palindrome = int(s + s[-2::-1])

                if palindrome >= n and is_prime(palindrome):
                    return palindrome

            digits += 1