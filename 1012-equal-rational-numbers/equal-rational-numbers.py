from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:

        def convert(x: str) -> Fraction:
            if '.' not in x:
                return Fraction(int(x), 1)

            integer, decimal = x.split('.')

            if '(' not in decimal:
                # Non-repeating decimal
                if decimal == "":
                    return Fraction(int(integer), 1)

                return Fraction(
                    int(integer) * 10 ** len(decimal) + int(decimal),
                    10 ** len(decimal)
                )

            non_repeat, repeat = decimal.split('(')
            repeat = repeat[:-1]  # remove ')'

            # Integer part + non-repeating part
            a = int(integer)
            b = int(non_repeat) if non_repeat else 0
            m = len(non_repeat)
            r = len(repeat)

            # Value:
            # integer + non_repeat / 10^m
            #       + repeat / (10^m * (10^r - 1))
            numerator = (
                a * 10 ** m * (10 ** r - 1)
                + b * (10 ** r - 1)
                + int(repeat)
            )

            denominator = 10 ** m * (10 ** r - 1)

            return Fraction(numerator, denominator)

        return convert(s) == convert(t)