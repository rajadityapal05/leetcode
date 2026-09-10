class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    a = nums[i]
                    b = nums[j]

                    remaining = [
                        nums[k] for k in range(len(nums))
                        if k != i and k != j
                    ]

                    results = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]

                    if b != 0:
                        results.append(a / b)

                    if a != 0:
                        results.append(b / a)

                    for value in results:
                        remaining.append(value)

                        if solve(remaining):
                            return True

                        remaining.pop()

            return False

        return solve([float(x) for x in cards])