
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = {}

        for a in nums1:
            for b in nums2:
                total = a + b
                count[total] = count.get(total, 0) + 1

        result = 0

        for c in nums3:
            for d in nums4:
                result += count.get(-(c + d), 0)

        return result
