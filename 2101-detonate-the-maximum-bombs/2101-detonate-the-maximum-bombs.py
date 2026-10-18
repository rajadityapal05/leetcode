from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, _ = bombs[j]

                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r ** 2:
                    graph[i].append(j)

        def dfs(node, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

            return len(visited)

        ans = 0

        for i in range(n):
            ans = max(ans, dfs(i, set()))

        return ans  