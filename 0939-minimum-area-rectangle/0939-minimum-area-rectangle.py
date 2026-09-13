class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = {(x, y) for x, y in points}
        n = len(points)

        answer = float("inf")

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # They must be diagonal corners.
                if x1 == x2 or y1 == y2:
                    continue

                # Check the other two corners.
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    answer = min(answer, area)

        return 0 if answer == float("inf") else answer