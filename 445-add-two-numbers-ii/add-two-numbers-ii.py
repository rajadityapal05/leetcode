class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1 = []
        stack2 = []

        # Put l1 values into stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # Put l2 values into stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        # Add from right to left
        while stack1 or stack2 or carry:

            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0

            total = a + b + carry

            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)

            new_node.next = result
            result = new_node

        return result