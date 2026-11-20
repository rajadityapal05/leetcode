
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result = 0

        for house in houses:
            i = bisect_left(heaters, house)

            right = float('inf')
            left = float('inf')

            if i < len(heaters):
                right = heaters[i] - house

            if i > 0:
                left = house - heaters[i - 1]

            nearest = min(left, right)
            result = max(result, nearest)

        return result
