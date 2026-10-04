class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # C(n + e - 1, e)
        # Maximum exponent is 13 because 2^13 <= 10^4.
        MAX_E = 14

        # factorials for combinations
        fact = [1] * (n + MAX_E + 1)
        inv_fact = [1] * (n + MAX_E + 1)

        for i in range(1, len(fact)):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)

        for i in range(len(fact) - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # Smallest prime factor
        spf = list(range(maxValue + 1))

        for i in range(2, int(maxValue ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        ans = 0

        for value in range(1, maxValue + 1):
            x = value
            ways = 1

            while x > 1:
                p = spf[x]
                e = 0

                while x % p == 0:
                    x //= p
                    e += 1

                # Number of ways for this prime exponent
                ways = ways * comb(n + e - 1, e) % MOD

            ans = (ans + ways) % MOD

        return ans