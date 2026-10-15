class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        count = 0

        for i in range(n // 2):
            if num[i] == '?':
                count += 1
            else:
                diff += int(num[i])

            if num[n - 1 - i] == '?':
                count -= 1
            else:
                diff -= int(num[n - 1 - i])

        return diff != -9 * count // 2 if count % 2 == 0 else True