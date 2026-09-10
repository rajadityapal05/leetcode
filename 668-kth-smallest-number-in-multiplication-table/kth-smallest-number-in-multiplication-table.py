class Solution:
    def findKthNumber(self, m, n, k):
        left = 1
        right = m * n

        while left < right:
            mid = (left + right) // 2

            count = 0

            for i in range(1, m + 1):
                count += min(n, mid // i)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left