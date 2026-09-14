class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        op = 0

        while n > 0:
            if op == 0:          # *
                stack[-1] *= n

            elif op == 1:        # /
                # Truncate toward zero
                if stack[-1] >= 0:
                    stack[-1] //= n
                else:
                    stack[-1] = -((-stack[-1]) // n)

            elif op == 2:        # +
                stack.append(n)

            else:                # -
                stack.append(-n)

            n -= 1
            op = (op + 1) % 4

        return sum(stack)