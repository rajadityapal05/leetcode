class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []
        n = len(num)

        def backtrack(index: int, expression: str, value: int, prev: int):
            if index == n:
                if value == target:
                    result.append(expression)
                return

            for end in range(index, n):
                # No leading zeros
                if end > index and num[index] == '0':
                    break

                current = int(num[index:end + 1])

                if index == 0:
                    backtrack(
                        end + 1,
                        str(current),
                        current,
                        current
                    )
                else:
                    # Addition
                    backtrack(
                        end + 1,
                        expression + "+" + str(current),
                        value + current,
                        current
                    )

                    # Subtraction
                    backtrack(
                        end + 1,
                        expression + "-" + str(current),
                        value - current,
                        -current
                    )

                    # Multiplication
                    backtrack(
                        end + 1,
                        expression + "*" + str(current),
                        value - prev + prev * current,
                        prev * current
                    )

        backtrack(0, "", 0, 0)

        return result