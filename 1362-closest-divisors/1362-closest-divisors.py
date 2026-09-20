class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        best = None
        min_diff = float('inf')

        for x in (num + 1, num + 2):
            a = int(x ** 0.5)

            while a > 0:
                if x % a == 0:
                    b = x // a
                    diff = b - a

                    if diff < min_diff:
                        min_diff = diff
                        best = [a, b]

                    break

                a -= 1

        return best