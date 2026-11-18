
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        count = 0
        current_end = float('-inf')

        for left, right in pairs:
            if left > current_end:
                count += 1
                current_end = right

        return count
