from functools import lru_cache


class Solution:
    def mostFrequentPrime(self, mat):
        m, n = len(mat), len(mat[0])

        directions = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        )

        @lru_cache(None)
        def is_prime(x):
            if x < 2:
                return False

            # Small primes
            if x == 2 or x == 3:
                return True

            if x % 2 == 0 or x % 3 == 0:
                return False

            # Miller-Rabin
            d = x - 1
            s = 0

            while d % 2 == 0:
                s += 1
                d //= 2

            for a in (2, 3):
                if a >= x:
                    continue

                y = pow(a, d, x)

                if y == 1 or y == x - 1:
                    continue

                for _ in range(s - 1):
                    y = (y * y) % x

                    if y == x - 1:
                        break
                else:
                    return False

            return True

        freq = {}

        for r in range(m):
            for c in range(n):
                for dr, dc in directions:

                    nr, nc = r, c
                    num = 0

                    while 0 <= nr < m and 0 <= nc < n:
                        num = num * 10 + mat[nr][nc]

                        if num > 10 and is_prime(num):
                            freq[num] = freq.get(num, 0) + 1

                        nr += dr
                        nc += dc

        if not freq:
            return -1

        # Highest frequency -> largest number on tie
        return max(freq, key=lambda x: (freq[x], x))