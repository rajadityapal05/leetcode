
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for word in words:
            forward = {}
            backward = {}
            match = True

            for p, w in zip(pattern, word):
                if p in forward:
                    if forward[p] != w:
                        match = False
                        break
                else:
                    forward[p] = w

                if w in backward:
                    if backward[w] != p:
                        match = False
                        break
                else:
                    backward[w] = p

            if match:
                result.append(word)

        return result
