
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()

                left = mid - stack[-1] if stack else mid + 1
                right = i - mid

                result += arr[mid] * left * right

            stack.append(i)

        return result % MOD
