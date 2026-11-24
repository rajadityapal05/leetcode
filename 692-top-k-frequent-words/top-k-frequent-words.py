
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap = []

        for word, count in freq.items():
            # Lower frequency has lower priority.
            # For equal frequency, lexicographically larger word
            # has lower priority.
            heapq.heappush(heap, (count, ReverseWord(word)))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap)[1].word)

        return result[::-1]


class ReverseWord:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word
