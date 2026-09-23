from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        # cost[i][j] = minimum distance if houses[i..j]
        # are served by one mailbox
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2

                for x in range(i, j + 1):
                    cost[i][j] += abs(houses[x] - houses[mid])

        # dp[b][i] = minimum distance to serve
        # first i houses using b mailboxes
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for b in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(b - 1, i):
                    dp[b][i] = min(
                        dp[b][i],
                        dp[b - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]