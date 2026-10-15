class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

                k = 1
                while i + 2 * k < m and j - k >= 0 and j + k < n:
                    total = 0

                    for t in range(k):
                        total += grid[i + t][j + t]
                        total += grid[i + k + t][j + k - t]
                        total += grid[i + 2 * k - t][j - t]
                        total += grid[i + k - t][j - k + t]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]