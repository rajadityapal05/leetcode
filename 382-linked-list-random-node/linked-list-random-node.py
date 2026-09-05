import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []

        current = head

        while current:
            self.values.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return random.choice(self.values)