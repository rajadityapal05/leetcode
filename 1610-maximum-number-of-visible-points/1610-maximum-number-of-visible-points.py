import math

class Solution:
    def visiblePoints(self, points, angle, location):
        x0, y0 = location
        angles = []
        same = 0

        for x, y in points:
            dx = x - x0
            dy = y - y0

            if dx == 0 and dy == 0:
                same += 1
            else:
                # Angle measured counterclockwise from east
                theta = math.degrees(math.atan2(dy, dx))

                # Convert to [0, 360)
                if theta < 0:
                    theta += 360

                angles.append(theta)

        angles.sort()

        # Duplicate the angles with +360 to handle wrap-around
        extended = angles + [a + 360 for a in angles]

        max_visible = 0
        left = 0

        for right in range(len(extended)):
            while extended[right] - extended[left] > angle:
                left += 1

            max_visible = max(max_visible, right - left + 1)

        return max_visible + same