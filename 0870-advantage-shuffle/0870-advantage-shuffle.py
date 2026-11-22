class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        sorted_nums2 = sorted(
            [(value, i) for i, value in enumerate(nums2)],
            reverse=True
        )

        left, right = 0, len(nums1) - 1
        ans = [0] * len(nums1)

        for num, i in sorted_nums2:
            if nums1[right] > num:
                ans[i] = nums1[right]
                right -= 1
            else:
                ans[i] = nums1[left]
                left += 1

        return ans