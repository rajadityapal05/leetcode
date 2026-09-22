class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        n = len(piles) // 3
        left = 0
        right = len(piles) - 1
        ans = 0

        for _ in range(n):
            # Alice takes the largest
            right -= 1

            # You take the next largest
            ans += piles[right]
            right -= 1

            # Bob effectively gets the smallest remaining pile
            left += 1

        return ans