class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def is_subsequence(a, b):
            i = 0

            for char in b:
                if i < len(a) and a[i] == char:
                    i += 1

            return i == len(a)

        strs.sort(key=len, reverse=True)

        for i, s in enumerate(strs):
            uncommon = True

            for j, t in enumerate(strs):
                if i != j and is_subsequence(s, t):
                    uncommon = False
                    break

            if uncommon:
                return len(s)

        return -1