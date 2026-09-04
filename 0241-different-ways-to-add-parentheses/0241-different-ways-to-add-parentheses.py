class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def solve(exp):
            results = []

            for i in range(len(exp)):
                if exp[i] in "+-*":
                    
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for a in left:
                        for b in right:
                            if exp[i] == "+":
                                results.append(a + b)
                            elif exp[i] == "-":
                                results.append(a - b)
                            else:
                                results.append(a * b)

            # If there was no operator, exp is just a number
            if not results:
                results.append(int(exp))

            return results

        return solve(expression)