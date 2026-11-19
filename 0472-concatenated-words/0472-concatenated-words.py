
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        def is_concatenated(word):
            n = len(word)

            # dp[i] = maximum number of words forming word[:i]
            dp = [-1] * (n + 1)
            dp[0] = 0

            for i in range(n):
                if dp[i] == -1:
                    continue

                node = root

                for j in range(i, n):
                    ch = word[j]

                    if ch not in node.children:
                        break

                    node = node.children[ch]

                    if node.is_end:
                        dp[j + 1] = max(dp[j + 1], dp[i] + 1)

            return dp[n] >= 2

        result = []

        for word in words:
            if is_concatenated(word):
                result.append(word)

        return result
