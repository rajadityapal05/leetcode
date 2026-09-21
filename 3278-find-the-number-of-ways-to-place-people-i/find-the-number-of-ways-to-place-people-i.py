class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2 = points[j]

                # A must be upper-left of B
                if x1 > x2 or y1 < y2:
                    continue

                valid = True

                # Check whether another point lies
                # inside or on the boundary of the rectangle.
                for k in range(n):
                    if k == i or k == j:
                        continue

                    x, y = points[k]

                    if x1 <= x <= x2 and y2 <= y <= y1:
                        valid = False
                        break

                if valid:
                    ans += 1

        return ans