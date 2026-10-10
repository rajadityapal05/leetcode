
class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        answer = []

        for x, y, r in queries:
            count = 0
            r2 = r * r

            for px, py in points:
                dx = px - x
                dy = py - y

                if dx * dx + dy * dy <= r2:
                    count += 1

            answer.append(count)

        return answer
