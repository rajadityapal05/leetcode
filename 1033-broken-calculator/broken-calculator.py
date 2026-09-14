class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0

        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

            operations += 1

        # Now target <= startValue.
        # We can only subtract in the forward direction.
        operations += startValue - target

        return operations