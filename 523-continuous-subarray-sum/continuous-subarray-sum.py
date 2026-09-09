class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder_index = {0: -1}

        total = 0

        for i in range(len(nums)):

            total += nums[i]

            remainder = total % k

            if remainder in remainder_index:

                previous_index = remainder_index[remainder]

                if i - previous_index >= 2:
                    return True

            else:
                remainder_index[remainder] = i

        return False