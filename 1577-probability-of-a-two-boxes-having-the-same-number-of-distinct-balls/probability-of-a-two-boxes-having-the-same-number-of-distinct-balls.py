class Solution:
    def getProbability(self, balls: list[int]) -> float:
        from math import comb
from typing import List


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2

        good = 0
        total = 0

        def dfs(
            i: int,
            box1: int,
            box2: int,
            distinct1: int,
            distinct2: int,
            ways: int
        ):
            nonlocal good, total

            # All colors distributed
            if i == len(balls):
                if box1 == n and box2 == n:
                    total += ways

                    if distinct1 == distinct2:
                        good += ways
                return

            count = balls[i]

            # Put x balls of this color in box 1
            for x in range(count + 1):
                y = count - x

                # Don't exceed box capacities
                if box1 + x > n or box2 + y > n:
                    continue

                new_distinct1 = distinct1 + (x > 0)
                new_distinct2 = distinct2 + (y > 0)

                dfs(
                    i + 1,
                    box1 + x,
                    box2 + y,
                    new_distinct1,
                    new_distinct2,
                    ways * comb(count, x)
                )

        dfs(0, 0, 0, 0, 0, 1)

        return good / total