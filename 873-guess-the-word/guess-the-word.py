class Solution:
    def findSecretWord(self, words: list[str], master: "Master") -> None:

        def matches(a, b):
            return sum(x == y for x, y in zip(a, b))

        candidates = words[:]

        for _ in range(30):
            # Choose the word that minimizes the largest
            # possible group of remaining candidates.
            best_word = candidates[0]
            best_score = float("inf")

            for word in candidates:
                groups = [0] * 7

                for other in candidates:
                    m = matches(word, other)
                    groups[m] += 1

                worst_group = max(groups)

                if worst_group < best_score:
                    best_score = worst_group
                    best_word = word

            score = master.guess(best_word)

            if score == 6:
                return

            # Keep only words that would produce the same
            # number of matches as our guess.
            candidates = [
                word for word in candidates
                if matches(best_word, word) == score
            ]