class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        answer = 0

        for i in range(len(points)):

            distance_count = {}

            x1, y1 = points[i]

            for j in range(len(points)):

                if i == j:
                    continue

                x2, y2 = points[j]

                dx = x1 - x2
                dy = y1 - y2

                distance = dx * dx + dy * dy

                distance_count[distance] = (
                    distance_count.get(distance, 0) + 1
                )

            for count in distance_count.values():
                answer += count * (count - 1)

        return answer