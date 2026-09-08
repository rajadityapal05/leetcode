import math

class Solution:
    def fractionAddition(self, expression: str) -> str:

        # Add + at the beginning if needed
        if expression[0] != '-':
            expression = '+' + expression

        result_num = 0
        result_den = 1

        i = 0

        while i < len(expression):

            # Read the sign
            sign = 1

            if expression[i] == '-':
                sign = -1

            i += 1

            # Read numerator
            numerator = 0

            while i < len(expression) and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1

            # Skip '/'
            i += 1

            # Read denominator
            denominator = 0

            while i < len(expression) and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1

            numerator *= sign

            # Add current fraction to result
            result_num = (
                result_num * denominator
                + numerator * result_den
            )

            result_den *= denominator

            # Simplify
            g = math.gcd(abs(result_num), result_den)

            result_num //= g
            result_den //= g

        return str(result_num) + "/" + str(result_den)