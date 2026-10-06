class Solution:
    def reinitializePermutation(self, n: int) -> int:
        pos = 1
        operations = 0

        while True:
            if pos < n // 2:
                pos = 2 * pos
            else:
                pos = 2 * (pos - n // 2) + 1

            operations += 1

            if pos == 1:
                return operations 