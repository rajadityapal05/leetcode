class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        values = []
        ops = []

        def merge(a, b, op):
            a0, a1 = a
            b0, b1 = b

            if op == '&':
                c0 = min(a0 + b0, a0 + b1, a1 + b0)
                c1 = min(a1 + b1, 1 + a1 + b0, 1 + a0 + b1)
            else:
                c0 = min(a0 + b0, 1 + a0 + b1, 1 + a1 + b0)
                c1 = min(a1 + b0, a0 + b1, a1 + b1)

            return (c0, c1)

        def reduce():
            op = ops.pop()
            b = values.pop()
            a = values.pop()
            values.append(merge(a, b, op))

        for ch in expression:
            if ch == '0':
                values.append((0, 1))
                while ops and ops[-1] in '&|' and len(values) >= 2:
                    reduce()

            elif ch == '1':
                values.append((1, 0))
                while ops and ops[-1] in '&|' and len(values) >= 2:
                    reduce()

            elif ch in '&|(':
                ops.append(ch)

            elif ch == ')':
                while ops[-1] != '(':
                    reduce()
                ops.pop()

                while ops and ops[-1] in '&|' and len(values) >= 2:
                    reduce()

        c0, c1 = values[0]
        return max(c0, c1)