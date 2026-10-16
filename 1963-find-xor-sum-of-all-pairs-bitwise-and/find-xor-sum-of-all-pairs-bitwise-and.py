class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor1 = 0
        xor2 = 0

        for x in arr1:
            xor1 ^= x

        for x in arr2:
            xor2 ^= x

        return xor1 & xor2 