class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            left = i + 1
            right = n - i

            total_subarrays = left * right

            odd_subarrays = (total_subarrays + 1) // 2

            ans += arr[i] * odd_subarrays

        return ans