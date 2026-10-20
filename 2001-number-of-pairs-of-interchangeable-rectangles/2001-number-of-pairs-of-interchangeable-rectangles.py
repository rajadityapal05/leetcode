class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import defaultdict
        from math import gcd

        count = defaultdict(int)
        pairs = 0

        for w, h in rectangles:
            g = gcd(w, h)
            ratio = (w // g, h // g)

            pairs += count[ratio]
            count[ratio] += 1

        return pairs 