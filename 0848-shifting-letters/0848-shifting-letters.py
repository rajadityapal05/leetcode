class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        result = []

        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26

            shifted = (ord(s[i]) - ord('a') + total) % 26
            result.append(chr(shifted + ord('a')))

        return ''.join(reversed(result))