class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(s)
        k = len(digits)
        ans = 0

        for length in range(1, m):
            ans += k ** length

        for i in range(m):
            count = sum(d < s[i] for d in digits)
            ans += count * (k ** (m - i - 1))

            if s[i] not in digits:
                return ans

        return ans + 1 