
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if len(word) > m * n:
            return False

        # Search pruning: check character frequencies
        from collections import Counter

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        for ch, count in word_count.items():
            if board_count[ch] < count:
                return False

        # Start with the less frequent end of the word
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= m or c < 0 or c >= n
                    or board[r][c] != word[idx]):
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Backtrack: restore original character
            board[r][c] = temp

            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
