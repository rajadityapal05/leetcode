class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]

        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n

        def dfs(x):
            if answer[x] != -1:
                return answer[x]

            answer[x] = x

            for person in graph[x]:
                candidate = dfs(person)
                if quiet[candidate] < quiet[answer[x]]:
                    answer[x] = candidate

            return answer[x]

        for i in range(n):
            dfs(i)

        return answer