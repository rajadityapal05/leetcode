from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        frequencies = Counter(deck).values()

        g = 0

        for freq in frequencies:
            g = gcd(g, freq)

        return g >= 2