class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)

        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        ans = 0

        # A palindrome root can have at most 9 digits because:
        # sqrt(10^18) = 10^9
        #
        # Generate palindromes by taking the first half and mirroring it.
        for length in range(1, 10):
            half_len = (length + 1) // 2

            start = 1 if length == 1 else 10 ** (half_len - 1)
            end = 10 ** half_len

            for half in range(start, end):
                s = str(half)

                if length % 2 == 0:
                    root = int(s + s[::-1])
                else:
                    root = int(s + s[-2::-1])

                square = root * root

                if square > R:
                    continue

                if square >= L and is_palindrome(square):
                    ans += 1

        return ans