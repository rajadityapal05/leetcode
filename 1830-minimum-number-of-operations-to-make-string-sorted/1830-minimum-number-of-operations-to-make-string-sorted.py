class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # frequency of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # inverse factorials
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        ans = 0

        for i in range(n):
            curr = ord(s[i]) - ord('a')

            # Number of smaller unused characters
            smaller = sum(freq[:curr])

            # Number of distinct permutations of the remaining characters
            ways = fact[n - i - 1]

            for c in range(26):
                ways = ways * inv_fact[freq[c]] % MOD

            ans = (ans + smaller * ways) % MOD

            # Remove current character
            freq[curr] -= 1

        return ans