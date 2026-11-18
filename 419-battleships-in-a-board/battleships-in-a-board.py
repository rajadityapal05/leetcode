
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    if r > 0 and board[r - 1][c] == 'X':
                        continue

                    if c > 0 and board[r][c - 1] == 'X':
                        continue

                    count += 1

        return count
