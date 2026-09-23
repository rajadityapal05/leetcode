import math
from typing import List


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        ans = 1
        eps = 1e-9

        for i in range(n):
            x1, y1 = darts[i]

            for j in range(i + 1, n):
                x2, y2 = darts[j]

                dx = x2 - x1
                dy = y2 - y1
                d2 = dx * dx + dy * dy

                # Two points cannot lie on a circle of radius r
                if d2 > 4 * r * r:
                    continue

                d = math.sqrt(d2)

                # Midpoint of the two points
                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                # Distance from midpoint to either possible center
                h = math.sqrt(r * r - (d / 2) ** 2)

                # Unit perpendicular vector
                px = -dy / d
                py = dx / d

                # First possible center
                cx1 = mx + px * h
                cy1 = my + py * h

                # Second possible center
                cx2 = mx - px * h
                cy2 = my - py * h

                count1 = 0
                count2 = 0

                for x, y in darts:
                    if (x - cx1) ** 2 + (y - cy1) ** 2 <= r * r + eps:
                        count1 += 1

                    if (x - cx2) ** 2 + (y - cy2) ** 2 <= r * r + eps:
                        count2 += 1

                ans = max(ans, count1, count2)

        return ans