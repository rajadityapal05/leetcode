import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.flipped = {}

    def flip(self) -> list[int]:

        # Pick one random position among remaining cells
        random_index = random.randrange(self.remaining)

        # Find the actual cell stored at this position
        actual_index = self.flipped.get(
            random_index,
            random_index
        )

        # Move the last available cell into this position
        self.remaining -= 1

        self.flipped[random_index] = self.flipped.get(
            self.remaining,
            self.remaining
        )

        # Convert 1D index back to (row, column)
        row = actual_index // self.n
        col = actual_index % self.n

        return [row, col]

    def reset(self) -> None:

        self.remaining = self.total
        self.flipped.clear()