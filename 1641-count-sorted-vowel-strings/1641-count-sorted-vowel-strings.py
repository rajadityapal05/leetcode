class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Number of combinations with repetition:
        # C(n + 5 - 1, 5 - 1) = C(n + 4, 4)
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24