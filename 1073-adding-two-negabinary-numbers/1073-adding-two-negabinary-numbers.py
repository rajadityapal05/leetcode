class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += arr1[i]
                i -= 1

            if j >= 0:
                total += arr2[j]
                j -= 1

            # Convert total into:
            # digit (0 or 1) + (-2) * new_carry
            digit = total & 1
            carry = -(total >> 1)

            result.append(digit)

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]