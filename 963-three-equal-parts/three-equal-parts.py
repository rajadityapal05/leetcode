
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones = sum(arr)

        if ones == 0:
            return [0, 2]

        if ones % 3 != 0:
            return [-1, -1]

        k = ones // 3

        first = second = third = -1
        count = 0

        for i in range(n):
            if arr[i] == 1:
                count += 1

                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        while third < n:
            if arr[first] != arr[second] or arr[second] != arr[third]:
                return [-1, -1]

            first += 1
            second += 1
            third += 1

        return [first - 1, second]
