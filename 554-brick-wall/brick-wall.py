from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        max_edges = 0
 
        for row in wall:
            position = 0

            for brick in row[:-1]:
                position += brick
                edges[position] += 1
                max_edges = max(max_edges, edges[position])

        return len(wall) - max_edges