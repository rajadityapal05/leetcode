class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        # For every divisor d > threshold,
        # connect all multiples of d.
        for d in range(threshold + 1, n + 1):
            first = d

            for multiple in range(2 * d, n + 1, d):
                union(first, multiple)

        return [find(a) == find(b) for a, b in queries] 