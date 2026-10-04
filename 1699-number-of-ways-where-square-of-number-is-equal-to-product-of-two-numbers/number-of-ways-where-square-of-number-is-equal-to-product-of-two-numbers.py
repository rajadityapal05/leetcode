from collections import Counter
from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(a, b):
            freq = Counter(b)
            ans = 0

            for x in a:
                target = x * x

                for i in range(len(b)):
                    if target % b[i] == 0:
                        need = target // b[i]

                        if need in freq:
                            if need == b[i]:
                                ans += freq[need] - 1
                            else:
                                ans += freq[need]

            return ans // 2

        return count(nums1, nums2) + count(nums2, nums1)