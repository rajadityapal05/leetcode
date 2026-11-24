
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values = set(nums)
        count = 0

        while head:
            if head.val in values and (head.next is None or head.next.val not in values):
                count += 1

            head = head.next

        return count
