class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7

        count = 0
        ans = 0

        for ch in s:
            if ch == '1':
                count += 1
                ans += count
            else:
                count = 0

        return ans % MOD