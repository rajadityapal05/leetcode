
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = [0] * 26

        for word in words2:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                required[i] = max(required[i], count[i])

        result = []

        for word in words1:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            if all(count[i] >= required[i] for i in range(26)):
                result.append(word)

        return result
