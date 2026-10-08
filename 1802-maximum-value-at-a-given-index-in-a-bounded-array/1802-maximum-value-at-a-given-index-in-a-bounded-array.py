class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def side_sum(x, length):
            # Minimum sum of `length` elements next to a peak x.
            # Values decrease by 1 until reaching 1.
            if x > length:
                # x-1, x-2, ..., x-length
                return (x - 1 + x - length) * length // 2
            else:
                # x-1, ..., 1, 1, 1, ...
                return x * (x - 1) // 2 + (length - (x - 1))

        def required_sum(x):
            left = side_sum(x, index)
            right = side_sum(x, n - index - 1)
            return left + x + right

        lo, hi = 1, maxSum

        while lo <= hi:
            mid = (lo + hi) // 2

            if required_sum(mid) <= maxSum:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi