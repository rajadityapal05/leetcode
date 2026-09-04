import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        result = ""

        k -= 1

        for i in range(n, 0, -1):
            block_size = math.factorial(i - 1)

            index = k // block_size

            result += str(numbers[index])
            numbers.pop(index)

            k %= block_size

        return result