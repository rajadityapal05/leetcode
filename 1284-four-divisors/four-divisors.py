class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        answer = 0

        for n in nums:
            divisor_count = 0
            divisor_sum = 0

            d = 1

            while d * d <= n:
                if n % d == 0:
                    q = n // d

                    divisor_count += 1
                    divisor_sum += d

                    # d and q are different divisors
                    if d != q:
                        divisor_count += 1
                        divisor_sum += q

                    if divisor_count > 4:
                        break

                d += 1

            if divisor_count == 4:
                answer += divisor_sum

        return answer