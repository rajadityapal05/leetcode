from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1

                slopes[(dx, dy)] += 1
                ans = max(ans, slopes[(dx, dy)] + 1)

        return ans