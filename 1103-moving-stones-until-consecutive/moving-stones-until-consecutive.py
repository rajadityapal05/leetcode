class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        x, y, z = sorted([a, b, c])

        if z - x == 2:
            return [0, 0]

        # One move is possible if an endpoint can jump
        # next to the middle stone.
        if y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2

        max_moves = (y - x - 1) + (z - y - 1)

        return [min_moves, max_moves]