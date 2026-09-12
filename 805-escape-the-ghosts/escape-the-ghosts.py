class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        my_distance = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            ghost_distance = abs(x - target[0]) + abs(y - target[1])

            if ghost_distance <= my_distance:
                return False

        return True