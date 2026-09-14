class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        n = len(nums)

        parent = list(range(n))
        size = [1] * n

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

            # Union by size
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        # factor -> index of a number that contains this factor
        factor_owner = {}

        for i, num in enumerate(nums):
            x = num
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:
                    if factor in factor_owner:
                        union(i, factor_owner[factor])
                    else:
                        factor_owner[factor] = i

                    while x % factor == 0:
                        x //= factor

                factor += 1

            # x is the remaining prime factor
            if x > 1:
                if x in factor_owner:
                    union(i, factor_owner[x])
                else:
                    factor_owner[x] = i

        return max(size[find(i)] for i in range(n))