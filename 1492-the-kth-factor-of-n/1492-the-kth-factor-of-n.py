class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []

        d = 1

        while d * d <= n:
            if n % d == 0:
                small.append(d)

                if d != n // d:
                    large.append(n // d)

            d += 1

        # Factors in ascending order:
        # small + reversed(large)
        if k <= len(small):
            return small[k - 1]

        k -= len(small)

        if k <= len(large):
            return large[-k]

        return -1