class Solution:
    def outerTrees(self, trees):
        if len(trees) <= 1:
            return trees

        trees.sort()

        def cross(o, a, b):
            return (
                (a[0] - o[0]) * (b[1] - o[1])
                - (a[1] - o[1]) * (b[0] - o[0])
            )

        # Lower hull
        lower = []

        for point in trees:
            while len(lower) >= 2 and cross(
                lower[-2], lower[-1], point
            ) < 0:
                lower.pop()

            lower.append(point)

        # Upper hull
        upper = []

        for point in reversed(trees):
            while len(upper) >= 2 and cross(
                upper[-2], upper[-1], point
            ) < 0:
                upper.pop()

            upper.append(point)

        # Remove duplicates
        points = set()

        for p in lower[:-1] + upper[:-1]:
            points.add(tuple(p))

        return [list(p) for p in points]