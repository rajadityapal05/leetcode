class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        vowels = set("aeiou")

        for i, ch in enumerate(word):
            if ch in vowels:
                ans += (i + 1) * (n - i)

        return ans