
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        xs = sorted(set(
            x
            for x1, y1, x2, y2 in rectangles
            for x in (x1, x2)
        ))

        ans = 0

        for i in range(len(xs) - 1):
            x1, x2 = xs[i], xs[i + 1]

            intervals = []

            for rx1, y1, rx2, y2 in rectangles:
                if rx1 <= x1 and rx2 >= x2:
                    intervals.append((y1, y2))

            if not intervals:
                continue

            intervals.sort()

            covered_y = 0
            start, end = intervals[0]

            for y1, y2 in intervals[1:]:
                if y1 <= end:
                    end = max(end, y2)
                else:
                    covered_y += end - start
                    start, end = y1, y2

            covered_y += end - start

            ans = (ans + (x2 - x1) * covered_y) % MOD

        return ans
