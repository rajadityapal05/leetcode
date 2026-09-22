class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate Fibonacci numbers <= k
        fib = [1, 1]

        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])

        count = 0

        # Greedily take the largest Fibonacci number
        for num in reversed(fib):
            if num <= k:
                k -= num
                count += 1

                if k == 0:
                    break

        return count