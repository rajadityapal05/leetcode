class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int
    ) -> bool:

        # Closest point on the rectangle to the circle center
        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2))

        # Squared distance from center to closest point
        dx = x - xCenter
        dy = y - yCenter

        return dx * dx + dy * dy <= radius * radius