class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = -1
        ans = 0
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if last == -1:
                    ans = i
                else:
                    ans = max(ans, (i - last) // 2)
                last = i

        return max(ans, n - 1 - last)