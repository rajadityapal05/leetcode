
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, remaining):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return

            if remaining <= 0:
                return

            if len(path) + (10 - start) < k:
                return

            for num in range(start, 10):
                if num > remaining:
                    break

                path.append(num)
                backtrack(num + 1, remaining - num)
                path.pop()

        backtrack(1, n)
        return result
