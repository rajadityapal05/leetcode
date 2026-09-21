class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even = 1   # Empty prefix sum = 0 (even)
        odd = 0

        prefix = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                # Current even prefix needs a previous odd prefix
                ans += odd
                even += 1
            else:
                # Current odd prefix needs a previous even prefix
                ans += even
                odd += 1

        return ans % MOD