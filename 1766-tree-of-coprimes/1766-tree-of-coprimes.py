from math import gcd

class Solution:
    def getCoprimes(self, nums, edges):
        n = len(nums)

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [-1] * n

        # best[value] = [deepest_depth, node]
        best = [[-1, -1] for _ in range(51)]

        def dfs(node, parent, depth):
            value = nums[node]

            # Find the closest coprime ancestor.
            max_depth = -1

            for v in range(1, 51):
                if best[v][1] != -1 and gcd(value, v) == 1:
                    if best[v][0] > max_depth:
                        max_depth = best[v][0]
                        ans[node] = best[v][1]

            # Add current node to the ancestor path.
            old = best[value]
            best[value] = [depth, node]

            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node, depth + 1)

            # Remove current node when leaving this subtree.
            best[value] = old

        dfs(0, -1, 0)

        return ans 