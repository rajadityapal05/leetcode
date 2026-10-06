from collections import deque

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        R, C = len(grid), len(grid[0])
        N = R * C

        mouse = cat = food = -1

        for r in range(R):
            for c in range(C):
                p = r * C + c
                if grid[r][c] == 'M':
                    mouse = p
                elif grid[r][c] == 'C':
                    cat = p
                elif grid[r][c] == 'F':
                    food = p

        # Generate legal moves.
        def moves(p, jump):
            r, c = divmod(p, C)
            res = [p]  # staying is allowed

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for d in range(1, jump + 1):
                    nr = r + dr * d
                    nc = c + dc * d

                    if not (0 <= nr < R and 0 <= nc < C):
                        break

                    if grid[nr][nc] == '#':
                        break

                    res.append(nr * C + nc)

            return res

        mouse_moves = [[] for _ in range(N)]
        cat_moves = [[] for _ in range(N)]

        valid = []

        for r in range(R):
            for c in range(C):
                if grid[r][c] != '#':
                    p = r * C + c
                    valid.append(p)
                    mouse_moves[p] = moves(p, mouseJump)
                    cat_moves[p] = moves(p, catJump)

        # state:
        #   (mouse position, cat position, turn)
        #
        # turn = 0 -> Mouse
        # turn = 1 -> Cat
        #
        # result:
        #   0 = unknown
        #   1 = Mouse wins
        #   2 = Cat wins

        def state(m, c, turn):
            return ((m * N + c) << 1) | turn

        total = N * N * 2

        result = bytearray(total)
        degree = [0] * total

        # Number of legal moves from every state.
        for m in valid:
            for c in valid:
                if m == c:
                    continue

                degree[state(m, c, 0)] = len(mouse_moves[m])
                degree[state(m, c, 1)] = len(cat_moves[c])

        q = deque()

        # --------------------------------------------------
        # Terminal states
        # --------------------------------------------------

        for c in valid:
            if c != food:
                # Mouse is on food.
                # Mouse has already won.
                s = state(food, c, 0)
                result[s] = 1
                q.append(s)

                s = state(food, c, 1)
                result[s] = 1
                q.append(s)

        for m in valid:
            if m != food:
                # Cat is on food.
                s = state(m, food, 0)
                result[s] = 2
                q.append(s)

                s = state(m, food, 1)
                result[s] = 2
                q.append(s)

        # Cat catches Mouse.
        for p in valid:
            if p != food:
                s = state(p, p, 0)
                result[s] = 2
                q.append(s)

                s = state(p, p, 1)
                result[s] = 2
                q.append(s)

        # --------------------------------------------------
        # Reverse BFS
        # --------------------------------------------------

        while q:
            s = q.popleft()

            turn = s & 1
            x = s >> 1

            m = x // N
            c = x % N

            winner = result[s]

            if turn == 0:
                # Current state is Mouse's turn.
                #
                # Previous move was Cat's.
                #
                # Find cat positions from which Cat could
                # have moved to c.
                for pc in valid:
                    if c not in cat_moves[pc]:
                        continue

                    prev = state(m, pc, 1)

                    if result[prev]:
                        continue

                    # Cat wants a Cat-winning successor.
                    if winner == 2:
                        result[prev] = 2
                        q.append(prev)
                    else:
                        degree[prev] -= 1

                        if degree[prev] == 0:
                            result[prev] = 1
                            q.append(prev)

            else:
                # Current state is Cat's turn.
                #
                # Previous move was Mouse's.
                for pm in valid:
                    if m not in mouse_moves[pm]:
                        continue

                    prev = state(pm, c, 0)

                    if result[prev]:
                        continue

                    # Mouse wants a Mouse-winning successor.
                    if winner == 1:
                        result[prev] = 1
                        q.append(prev)
                    else:
                        degree[prev] -= 1

                        if degree[prev] == 0:
                            result[prev] = 2
                            q.append(prev)

        return result[state(mouse, cat, 0)] == 1