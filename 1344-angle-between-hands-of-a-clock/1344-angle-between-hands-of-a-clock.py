class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Minute hand: 6 degrees per minute
        minute_angle = minutes * 6

        # Hour hand: 30 degrees per hour + 0.5 degrees per minute
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # Difference between the two hands
        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle
        return min(angle, 360 - angle)