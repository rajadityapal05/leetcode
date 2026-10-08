class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        ans = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]

            while stack:
                j = stack[-1]

                # Car i cannot catch car j
                if speed <= cars[j][1]:
                    stack.pop()
                    continue

                # Time for i to catch j
                t = (cars[j][0] - pos) / (speed - cars[j][1])

                # j does not collide with anyone before i catches it
                if ans[j] == -1 or t <= ans[j]:
                    ans[i] = t
                    break

                # j collides with another car first,
                # so i may need to target that fleet instead.
                stack.pop()

            stack.append(i)

        return ans