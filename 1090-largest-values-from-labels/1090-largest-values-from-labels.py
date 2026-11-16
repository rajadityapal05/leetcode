
from typing import List
from collections import defaultdict

class Solution:
    def largestValsFromLabels(
        self,
        values: List[int],
        labels: List[int],
        numWanted: int,
        useLimit: int
    ) -> int:

        items = sorted(zip(values, labels), reverse=True)

        count = defaultdict(int)
        total = 0
        selected = 0

        for value, label in items:
            if count[label] < useLimit:
                total += value
                count[label] += 1
                selected += 1

                if selected == numWanted:
                    break

        return total
