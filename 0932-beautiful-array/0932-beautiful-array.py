class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        result = [1]

        while len(result) < n:
            # Generate odd numbers
            odds = [2 * x - 1 for x in result if 2 * x - 1 <= n]

            # Generate even numbers
            evens = [2 * x for x in result if 2 * x <= n]

            result = odds + evens

        return result