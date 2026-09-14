from collections import defaultdict
from math import sqrt


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        n = len(points)

        # (midpoint_x * 2, midpoint_y * 2, diagonal_length^2)
        groups = defaultdict(list)

        # Generate all possible diagonals
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                mid_x = x1 + x2
                mid_y = y1 + y2
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

                groups[(mid_x, mid_y, dist_sq)].append((i, j))

        answer = float("inf")

        # Every two diagonals in the same group form a rectangle
        for diagonals in groups.values():
            for a in range(len(diagonals)):
                i, j = diagonals[a]

                x1, y1 = points[i]
                x2, y2 = points[j]

                for b in range(a + 1, len(diagonals)):
                    k, l = diagonals[b]

                    x3, y3 = points[k]
                    x4, y4 = points[l]

                    # Adjacent side lengths from point i
                    side1 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    side2 = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)

                    area = side1 * side2
                    answer = min(answer, area)

        return 0 if answer == float("inf") else answer