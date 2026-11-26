
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()

        for num in arr:
            next_set = {num}

            for value in current:
                next_set.add(value | num)

            current = next_set
            result.update(current)

        return len(result)
