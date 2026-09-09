class Solution:
    def nearestPalindromic(self, n):
        length = len(n)

        # Special cases
        if n == "1":
            return "0"

        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        candidates = set()

        # Boundary candidates
        candidates.add(10 ** (length - 1) - 1)
        candidates.add(10 ** length + 1)

        # Try prefix - 1, prefix, prefix + 1
        for p in [prefix - 1, prefix, prefix + 1]:
            s = str(p)

            if length % 2 == 0:
                palindrome = s + s[::-1]
            else:
                palindrome = s + s[-2::-1]

            candidates.add(int(palindrome))

        original = int(n)

        # Remove n itself
        candidates.discard(original)

        # Find closest
        answer = None

        for candidate in candidates:
            if answer is None:
                answer = candidate
            else:
                diff1 = abs(candidate - original)
                diff2 = abs(answer - original)

                if diff1 < diff2 or (diff1 == diff2 and candidate < answer):
                    answer = candidate

        return str(answer)