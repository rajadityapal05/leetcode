class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # First pass: Calculate next states
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] in (1, 2):
                            live_neighbors += 1

                # Apply Game of Life rules
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2

                else:
                    if live_neighbors == 3:
                        board[i][j] = 3

        # Second pass: Finalize all cell states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1 