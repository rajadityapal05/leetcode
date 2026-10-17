from typing import List

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        total = sum(nums)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Build traversal order without recursion
        parent = [-1] * n
        order = [0]

        for node in order:
            for nei in graph[node]:
                if nei != parent[node]:
                    parent[nei] = node
                    order.append(nei)

        # Try the maximum possible number of components first
        for k in range(n, 0, -1):
            if total % k != 0:
                continue

            target = total // k

            if target < max(nums):
                continue

            subtree = nums[:]
            possible = True

            for node in reversed(order):
                if subtree[node] > target:
                    possible = False
                    break

                if subtree[node] == target:
                    subtree[node] = 0

                if parent[node] != -1:
                    subtree[parent[node]] += subtree[node]

            if possible and subtree[0] == 0:
                return k - 1

        return 0