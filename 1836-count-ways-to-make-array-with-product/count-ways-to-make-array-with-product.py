from typing import List

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        MAX = 10000
        MAX_E = 14

        # factorials
        fact = [1] * (MAX + MAX_E + 1)
        inv_fact = [1] * (MAX + MAX_E + 1)

        for i in range(1, len(fact)):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)

        for i in range(len(fact) - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        # Smallest prime factor
        spf = list(range(MAX + 1))

        for i in range(2, int(MAX ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        ans = []

        for n, k in queries:
            ways = 1
            x = k

            while x > 1:
                p = spf[x]
                exponent = 0

                while x % p == 0:
                    x //= p
                    exponent += 1

                ways = ways * comb(n + exponent - 1, exponent) % MOD

            ans.append(ways)

        return ans 