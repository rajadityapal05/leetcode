class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7

        ans = 0
        count = 0
        prev = ''

        for ch in s:
            if ch == prev:
                count += 1
            else:
                count = 1
                prev = ch

            ans = (ans + count) % MOD

        return ans