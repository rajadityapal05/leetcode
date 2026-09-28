import math

class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        # Start at the centroid
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)

        def total_distance(x, y):
            return sum(
                math.hypot(x - px, y - py)
                for px, py in positions
            )

        step = 100.0
        best = total_distance(x, y)

        # Gradient descent / hill climbing
        while step > 1e-7:
            improved = False

            for dx, dy in ((step, 0), (-step, 0),
                           (0, step), (0, -step)):
                nx = x + dx
                ny = y + dy

                dist = total_distance(nx, ny)

                if dist < best:
                    x, y = nx, ny
                    best = dist
                    improved = True
                    break

            if not improved:
                step *= 0.5

        return best