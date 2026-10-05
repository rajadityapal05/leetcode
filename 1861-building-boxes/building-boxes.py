class Solution:
    def minimumBoxes(self, n: int) -> int:
        # Find the largest complete pyramid
        k = 0
        total = 0

        while total + (k + 1) * (k + 2) // 2 <= n:
            k += 1
            total += k * (k + 1) // 2

        # Boxes touching the floor in the complete pyramid
        floor = k * (k + 1) // 2

        # Remaining boxes
        remaining = n - total

        # Add boxes to the next layer
        x = 0
        while remaining > 0:
            x += 1
            remaining -= x

        return floor + x  