
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        parent = list(range(4 * n * n))
        rank = [0] * (4 * n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x

            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

            return True

        regions = 4 * n * n

        for r in range(n):
            for c in range(n):
                base = 4 * (r * n + c)

                top = base
                right = base + 1
                bottom = base + 2
                left = base + 3

                # Connections inside the current cell
                if grid[r][c] == ' ':
                    union(top, right)
                    union(right, bottom)
                    union(bottom, left)

                elif grid[r][c] == '/':
                    union(top, left)
                    union(right, bottom)

                else:  # Backslash '\'
                    union(top, right)
                    union(bottom, left)

                # Connect to the cell on the right
                if c + 1 < n:
                    next_left = 4 * (r * n + c + 1) + 3
                    if union(right, next_left):
                        regions -= 1

                # Connect to the cell below
                if r + 1 < n:
                    next_top = 4 * ((r + 1) * n + c)
                    if union(bottom, next_top):
                        regions -= 1

        # Count the remaining connected components
        return len({find(i) for i in range(4 * n * n)})
