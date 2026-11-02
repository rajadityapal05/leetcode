class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        for i, citation in enumerate(citations):
            if citation < i + 1:
                return i

        return len(citations)