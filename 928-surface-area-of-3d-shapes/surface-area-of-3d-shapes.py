class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h == 0:
                    continue

                # Top + bottom
                area += 2

                # Four sides
                area += 4 * h

                # Shared faces with the cell below
                if i + 1 < n:
                    area -= 2 * min(h, grid[i + 1][j])

                # Shared faces with the cell to the right
                if j + 1 < n:
                    area -= 2 * min(h, grid[i][j + 1])

        return area