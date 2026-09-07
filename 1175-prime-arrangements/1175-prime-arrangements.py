class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        MOD = 10**9 + 7

        prime_count = 0

        for num in range(2, n + 1):

            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_count += 1

        non_prime_count = n - prime_count

        prime_factorial = 1
        for i in range(1, prime_count + 1):
            prime_factorial = (prime_factorial * i) % MOD

        non_prime_factorial = 1
        for i in range(1, non_prime_count + 1):
            non_prime_factorial = (non_prime_factorial * i) % MOD

        return (prime_factorial * non_prime_factorial) % MOD