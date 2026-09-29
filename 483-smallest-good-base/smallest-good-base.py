class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        # Maximum possible number of 1s
        max_len = n.bit_length()

        # Try longer representations first
        for length in range(max_len, 2, -1):
            # n = 1 + k + k^2 + ... + k^(length-1)
            # k^(length-1) <= n, so estimate k
            k = int(n ** (1 / (length - 1)))

            # Floating-point estimation may be off by 1
            for base in (k, k + 1):
                if base < 2:
                    continue

                total = 0
                for _ in range(length):
                    total = total * base + 1
                    if total > n:
                        break

                if total == n:
                    return str(base)

        # If no length >= 3 works, n = 11 in base n-1
        return str(n - 1)