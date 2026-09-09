class Solution:
    def findMinDifference(self, timePoints):
        times = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            times.append(h * 60 + m)

        times.sort()

        ans = 1440  # minutes in a day

        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i - 1])

        # Difference across midnight
        ans = min(ans, 1440 - times[-1] + times[0])

        return ans