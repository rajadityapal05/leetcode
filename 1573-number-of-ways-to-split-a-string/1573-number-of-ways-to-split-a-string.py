class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7

        total_ones = s.count('1')

        # Cannot divide the 1s equally among 3 parts
        if total_ones % 3 != 0:
            return 0

        # All zeros: choose any 2 cut positions
        if total_ones == 0:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % MOD

        target = total_ones // 3

        ones = 0
        first = 0
        second = 0

        for ch in s:
            if ch == '1':
                ones += 1

            # Number of possible cuts after the first group
            if ones == target:
                first += 1

            # Number of possible cuts after the second group
            if ones == 2 * target:
                second += 1

        return (first * second) % MOD