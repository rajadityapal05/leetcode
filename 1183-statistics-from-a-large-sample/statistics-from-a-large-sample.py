class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        total = sum(count)
        total_sum = sum(i * count[i] for i in range(256))

        # Minimum and maximum
        minimum = next(i for i in range(256) if count[i] > 0)
        maximum = next(i for i in range(255, -1, -1) if count[i] > 0)

        # Mean
        mean = total_sum / total

        # Mode
        mode = max(range(256), key=lambda i: count[i])

        # Median
        mid1 = (total + 1) // 2
        mid2 = (total + 2) // 2

        cumulative = 0
        median1 = median2 = 0

        for i in range(256):
            cumulative += count[i]

            if cumulative >= mid1 and median1 == 0:
                median1 = i

            if cumulative >= mid2:
                median2 = i
                break

        median = (median1 + median2) / 2

        return [float(minimum), float(maximum), mean, median, float(mode)]