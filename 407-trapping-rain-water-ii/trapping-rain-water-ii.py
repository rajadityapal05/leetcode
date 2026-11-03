import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # Add all boundary cells
        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(1, n - 1):
            for i in (0, m - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            height, i, j = heapq.heappop(heap)

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    next_height = heightMap[ni][nj]

                    if next_height < height:
                        water += height - next_height

                    heapq.heappush(
                        heap,
                        (max(height, next_height), ni, nj)
                    )

        return water