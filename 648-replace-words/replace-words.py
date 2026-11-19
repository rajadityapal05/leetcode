
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()

        # Build the Trie
        for word in dictionary:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.is_end = True

        # Find the shortest matching root
        def find_root(word):
            node = root
            prefix = ""

            for ch in word:
                if ch not in node.children:
                    return word

                node = node.children[ch]
                prefix += ch

                if node.is_end:
                    return prefix

            return word

        return " ".join(find_root(word) for word in sentence.split())
