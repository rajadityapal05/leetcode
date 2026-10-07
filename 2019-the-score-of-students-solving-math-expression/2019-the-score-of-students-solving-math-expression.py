class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        nums = list(map(int, s[::2]))
        ops = list(s[1::2])
        n = len(nums)

        # Correct answer: multiplication before addition
        correct = nums[0]
        total = 0

        for i, op in enumerate(ops):
            if op == '*':
                correct *= nums[i + 1]
            else:
                total += correct
                correct = nums[i + 1]

        correct += total

        # dp[i][j] = all possible results from nums[i...j]
        dp = [[set() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i].add(nums[i])

        # Length of interval
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                for mid in range(left, right):
                    op = ops[mid]

                    for a in dp[left][mid]:
                        for b in dp[mid + 1][right]:
                            if op == '+':
                                value = a + b
                            else:
                                value = a * b

                            # Answers are at most 1000.
                            # With only + and *, values can never decrease,
                            # so larger values can be discarded.
                            if value <= 1000:
                                dp[left][right].add(value)

        possible = dp[0][n - 1]

        score = 0

        for answer in answers:
            if answer == correct:
                score += 5
            elif answer in possible:
                score += 2

        return score