
from typing import List
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = []

        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - x for x in row)

            patterns.append(pattern)

        return max(Counter(patterns).values())
