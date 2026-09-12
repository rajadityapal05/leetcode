class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows - 2):
            for c in range(cols - 2):

                # Center must be 5
                if grid[r + 1][c + 1] != 5:
                    continue

                # Check numbers 1 to 9 are distinct
                seen = set()
                valid = True

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        value = grid[i][j]

                        if value < 1 or value > 9 or value in seen:
                            valid = False
                            break

                        seen.add(value)

                    if not valid:
                        break

                if not valid:
                    continue

                # Check rows
                if any(
                    sum(grid[i][c:c + 3]) != 15
                    for i in range(r, r + 3)
                ):
                    continue

                # Check columns
                if any(
                    sum(grid[r + i][j] for i in range(3)) != 15
                    for j in range(c, c + 3)
                ):
                    continue

                # Check diagonals
                if (
                    grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15
                    or
                    grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
                ):
                    continue

                result += 1

        return result