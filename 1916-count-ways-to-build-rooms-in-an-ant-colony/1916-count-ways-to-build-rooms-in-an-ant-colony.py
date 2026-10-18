from typing import List

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)

        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[prevRoom[i]].append(i)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # Obtain traversal order without recursion
        order = [0]
        for node in order:
            order.extend(graph[node])

        size = [1] * n
        ways = [1] * n

        # Process children before parents
        for node in reversed(order):
            total = 0
            result = 1

            for child in graph[node]:
                result = result * ways[child] % MOD
                result = result * inv_fact[size[child]] % MOD
                total += size[child]

            size[node] = total + 1
            ways[node] = result * fact[total] % MOD

        return ways[0]