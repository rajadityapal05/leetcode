
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        vowels = set("aeiou")

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        def devowel(word):
            return ''.join(
                '*' if ch in vowels else ch
                for ch in word
            )

        # Build lookup maps
        for word in wordlist:
            lower = word.lower()

            case_map.setdefault(lower, word)
            vowel_map.setdefault(devowel(lower), word)

        result = []

        for query in queries:
            lower = query.lower()

            if query in exact:
                result.append(query)

            elif lower in case_map:
                result.append(case_map[lower])

            else:
                pattern = devowel(lower)
                result.append(vowel_map.get(pattern, ""))

        return result
