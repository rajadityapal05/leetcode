class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        result = 0

        for j in range(n):
            ones = 0

            for i in range(m):
                bit = grid[i][j]

                # First column must always be treated as all 1s.
                if j == 0:
                    bit = 1
                elif grid[i][0] == 0:
                    bit = 1 - bit

                ones += bit

            # Choose the better column orientation.
            result += max(ones, m - ones) * (1 << (n - j - 1))

        return result