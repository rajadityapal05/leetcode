class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1

        while i >= 0 and k > 0:
            num[i] += k % 10
            k //= 10

            if num[i] >= 10:
                num[i] -= 10
                k += 1

            i -= 1

        # If k still has digits left
        while k > 0:
            num.insert(0, k % 10)
            k //= 10

        return num