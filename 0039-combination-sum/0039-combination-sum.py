from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    break

                path.append(num)
                backtrack(i, remaining - num, path)
                path.pop()

        backtrack(0, target, [])
        return result