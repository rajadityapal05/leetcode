
from math import isqrt

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a * a + b * b
                c = isqrt(c_squared)

                if c <= n and c * c == c_squared:
                    ans += 1

        return ans
