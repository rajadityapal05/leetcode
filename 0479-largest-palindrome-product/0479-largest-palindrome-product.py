class Solution:
    def largestPalindrome(self, n: int) -> int:

        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = 10 ** (n - 1)

        for left in range(upper, lower - 1, -1):

            s = str(left)

            palindrome = int(s + s[::-1])

            factor = upper

            while factor * factor >= palindrome:

                if palindrome % factor == 0:

                    other = palindrome // factor

                    if lower <= other <= upper:
                        return palindrome % 1337

                factor -= 1

        return 0