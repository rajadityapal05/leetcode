import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:

        angle = random.uniform(0, 2 * math.pi)

        distance = self.radius * math.sqrt(random.random())

        x = self.x_center + distance * math.cos(angle)
        y = self.y_center + distance * math.sin(angle)

        return [x, y]