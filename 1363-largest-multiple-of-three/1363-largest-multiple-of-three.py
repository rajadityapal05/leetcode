class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = [0] * 10

        for d in digits:
            cnt[d] += 1

        total = sum(d * cnt[d] for d in range(10))
        remainder = total % 3

        def remove_one(rem):
            for d in range(rem, 10, 3):
                if cnt[d]:
                    cnt[d] -= 1
                    return True
            return False

        def remove_two(rem):
            removed = 0

            for d in range(rem, 10, 3):
                while cnt[d] and removed < 2:
                    cnt[d] -= 1
                    removed += 1

            return removed == 2

        if remainder == 1:
            # Remove one digit with remainder 1,
            # otherwise remove two digits with remainder 2.
            if not remove_one(1):
                remove_two(2)

        elif remainder == 2:
            # Remove one digit with remainder 2,
            # otherwise remove two digits with remainder 1.
            if not remove_one(2):
                remove_two(1)

        # Build answer in descending order
        result = []

        for d in range(9, -1, -1):
            result.append(str(d) * cnt[d])

        ans = ''.join(result)

        # No digits left
        if not ans:
            return ""

        # If everything is zero, return exactly "0"
        if ans[0] == '0':
            return "0"

        return ans