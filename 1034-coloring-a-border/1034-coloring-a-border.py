
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original = grid[row][col]

        visited = set()
        border = []

        def dfs(r, c):
            visited.add((r, c))
            is_border = False

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_border = True
                elif grid[nr][nc] != original:
                    is_border = True
                elif (nr, nc) not in visited:
                    dfs(nr, nc)

            if is_border:
                border.append((r, c))

        dfs(row, col)

        for r, c in border:
            grid[r][c] = color

        return grid
