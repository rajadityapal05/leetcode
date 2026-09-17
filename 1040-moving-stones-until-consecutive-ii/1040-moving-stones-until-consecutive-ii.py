class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)

        # Maximum moves
        max_moves = max(
            stones[-2] - stones[0],
            stones[-1] - stones[1]
        ) - (n - 2)

        # Minimum moves using a sliding window
        min_moves = n

        left = 0

        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1

            count = right - left + 1

            # Special case:
            # n-1 stones occupy n-1 consecutive positions,
            # while the remaining stone is too far away.
            if count == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - count)

        return [min_moves, max_moves]