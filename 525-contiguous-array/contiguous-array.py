class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first_seen:
                max_length = max(max_length, i - first_seen[balance])
            else:
                first_seen[balance] = i

        return max_length