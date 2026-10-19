class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = 0
        floors = 0

        while floors < n:
            moves += 1
            floors += moves

        return moves 