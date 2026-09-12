class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)

        # Check structural validity
        for i in range(n):
            for j in range(n):
                if board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]:
                    return -1

        # Count 1s in first row and first column
        row_ones = sum(board[0])
        col_ones = sum(board[i][0] for i in range(n))

        # For a chessboard, number of 1s must be n//2 or (n+1)//2
        if not (n // 2 <= row_ones <= (n + 1) // 2):
            return -1

        if not (n // 2 <= col_ones <= (n + 1) // 2):
            return -1

        # Count mismatches against alternating pattern
        row_mismatch = sum(
            board[0][i] != i % 2
            for i in range(n)
        )

        col_mismatch = sum(
            board[i][0] != i % 2
            for i in range(n)
        )

        # For odd n, only the pattern with the majority bit
        # in the first position is possible.
        if n % 2:
            if row_mismatch % 2:
                row_mismatch = n - row_mismatch

            if col_mismatch % 2:
                col_mismatch = n - col_mismatch

        else:
            row_mismatch = min(row_mismatch, n - row_mismatch)
            col_mismatch = min(col_mismatch, n - col_mismatch)

        return (row_mismatch + col_mismatch) // 2