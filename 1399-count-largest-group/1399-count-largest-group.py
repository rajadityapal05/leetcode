class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        max_size = max(groups.values())

        return sum(size == max_size for size in groups.values())