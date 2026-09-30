class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []

        for num in range(left, right + 1):
            x = num
            valid = True

            while x:
                digit = x % 10

                # 0 cannot be a divisor
                if digit == 0 or num % digit != 0:
                    valid = False
                    break

                x //= 10

            if valid:
                result.append(num)

        return result