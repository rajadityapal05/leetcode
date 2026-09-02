class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        indexes = [0] * len(primes)

        for i in range(1, n):
            candidates = []

            for j in range(len(primes)):
                candidates.append(ugly[indexes[j]] * primes[j])

            ugly[i] = min(candidates)

            for j in range(len(primes)):
                if candidates[j] == ugly[i]:
                    indexes[j] += 1

        return ugly[n - 1]