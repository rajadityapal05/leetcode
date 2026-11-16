
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        ans = 0

        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                ans += mid * min(stack[-1], num)

            stack.append(num)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans
