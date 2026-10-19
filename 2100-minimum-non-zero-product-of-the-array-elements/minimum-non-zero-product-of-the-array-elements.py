
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7

        maximum = (1 << p) - 1
        base = maximum - 1
        exponent = maximum // 2

        return (maximum * pow(base, exponent, MOD)) % MOD
