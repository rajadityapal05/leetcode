class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0

        for i in range(n):
            value = 2 * i + 1

            if value < n:
                operations += n - value

        return operations