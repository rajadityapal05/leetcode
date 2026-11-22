class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = {(x, y) for x, y in obstacles}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        direction = 0
        max_distance = 0

        for cmd in commands:
            if cmd == -2:
                direction = (direction + 3) % 4

            elif cmd == -1:
                direction = (direction + 1) % 4

            else:
                dx, dy = directions[direction]

                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny

                    max_distance = max(
                        max_distance,
                        x * x + y * y
                    )

        return max_distance