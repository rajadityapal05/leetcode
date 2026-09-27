class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(x):
            count = 0

            while x:
                x //= 5
                count += x

            return count

        # Find the first x such that f(x) >= k
        left, right = 0, 5 * (k + 1)

        while left < right:
            mid = (left + right) // 2

            if trailing_zeroes(mid) < k:
                left = mid + 1
            else:
                right = mid

        # If f(left) == k, exactly 5 consecutive values
        # have k trailing zeroes. Otherwise none do.
        return 5 if trailing_zeroes(left) == k else 0