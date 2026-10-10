
from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        max_num = max(nums)
        present = [False] * (max_num + 1)

        for num in nums:
            present[num] = True

        answer = 0

        for target in range(1, max_num + 1):
            current_gcd = 0

            for multiple in range(target, max_num + 1, target):
                if present[multiple]:
                    current_gcd = gcd(current_gcd, multiple)

                    if current_gcd == target:
                        answer += 1
                        break

        return answer
