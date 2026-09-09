class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        # Parse num1
        a, b = num1[:-1].split('+')
        a = int(a)
        b = int(b)

        # Parse num2
        c, d = num2[:-1].split('+')
        c = int(c)
        d = int(d)

        # Multiply
        real = a * c - b * d
        imaginary = a * d + b * c

        return str(real) + "+" + str(imaginary) + "i"