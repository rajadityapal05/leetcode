
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            lower_word = word.lower()

            for row in rows:
                if all(ch in row for ch in lower_word):
                    result.append(word)
                    break

        return result
