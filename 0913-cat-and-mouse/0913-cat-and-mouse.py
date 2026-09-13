class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        from collections import deque

class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n = len(graph)

        # color[m][c][turn]
        # 0 = draw/unknown
        # 1 = mouse wins
        # 2 = cat wins
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # Number of legal moves from each state.
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = sum(
                    nxt != 0 for nxt in graph[c]
                )

        queue = deque()

        # Mouse reaches the hole.
        for c in range(1, n):
            for turn in range(2):
                color[0][c][turn] = 1
                queue.append((0, c, turn, 1))

        # Cat catches Mouse.
        for pos in range(1, n):
            for turn in range(2):
                color[pos][pos][turn] = 2
                queue.append((pos, pos, turn, 2))

        while queue:
            mouse, cat, turn, result = queue.popleft()

            if turn == 0:
                # Current turn is Mouse.
                # Therefore the previous turn was Cat.
                for prev_cat in graph[cat]:
                    if prev_cat == 0:
                        continue

                    prev_mouse = mouse
                    prev_turn = 1

                    if color[prev_mouse][prev_cat][prev_turn] != 0:
                        continue

                    # Cat can choose this move and force a Cat win.
                    if result == 2:
                        color[prev_mouse][prev_cat][prev_turn] = 2
                        queue.append(
                            (prev_mouse, prev_cat, prev_turn, 2)
                        )
                    else:
                        degree[prev_mouse][prev_cat][prev_turn] -= 1

                        # Every move leads to a Mouse win,
                        # so Cat loses.
                        if degree[prev_mouse][prev_cat][prev_turn] == 0:
                            color[prev_mouse][prev_cat][prev_turn] = 1
                            queue.append(
                                (prev_mouse, prev_cat, prev_turn, 1)
                            )

            else:
                # Current turn is Cat.
                # Therefore the previous turn was Mouse.
                for prev_mouse in graph[mouse]:
                    prev_cat = cat
                    prev_turn = 0

                    if color[prev_mouse][prev_cat][prev_turn] != 0:
                        continue

                    # Mouse can choose this move and force a Mouse win.
                    if result == 1:
                        color[prev_mouse][prev_cat][prev_turn] = 1
                        queue.append(
                            (prev_mouse, prev_cat, prev_turn, 1)
                        )
                    else:
                        degree[prev_mouse][prev_cat][prev_turn] -= 1

                        # Every move leads to a Cat win,
                        # so Mouse loses.
                        if degree[prev_mouse][prev_cat][prev_turn] == 0:
                            color[prev_mouse][prev_cat][prev_turn] = 2
                            queue.append(
                                (prev_mouse, prev_cat, prev_turn, 2)
                            )

        return color[1][2][0]