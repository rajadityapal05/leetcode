
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(starts, visited):
            stack = starts[:]

            for r, c in stack:
                visited[r][c] = True

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n
                            and not visited[nr][nc]
                            and heights[nr][nc] >= heights[r][c]):

                        visited[nr][nc] = True
                        stack.append((nr, nc))

        # Pacific Ocean: top row and left column
        pacific_starts = (
            [(0, c) for c in range(n)] +
            [(r, 0) for r in range(m)]
        )

        # Atlantic Ocean: bottom row and right column
        atlantic_starts = (
            [(m - 1, c) for c in range(n)] +
            [(r, n - 1) for r in range(m)]
        )

        dfs(pacific_starts, pacific)
        dfs(atlantic_starts, atlantic)

        # Return cells reachable from both oceans
        result = []

        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result
