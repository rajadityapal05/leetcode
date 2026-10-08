class Solution:
    def countNicePairs(self, nums):
        MOD = 10**9 + 7
        freq = {}
        ans = 0

        for x in nums:
            rev = int(str(x)[::-1])
            key = x - rev

            # Every previous number with the same key
            # forms a nice pair with x.
            ans = (ans + freq.get(key, 0)) % MOD

            freq[key] = freq.get(key, 0) + 1

        return ans