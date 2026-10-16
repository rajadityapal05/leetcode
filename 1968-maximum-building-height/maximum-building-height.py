class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + x2 - x1)

        for i in range(len(restrictions) - 2, -1, -1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + x2 - x1)

        ans = 0

        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            peak = (h1 + h2 + x2 - x1) // 2
            ans = max(ans, peak)

        last_id, last_height = restrictions[-1]
        ans = max(ans, last_height + n - last_id)

        return ans