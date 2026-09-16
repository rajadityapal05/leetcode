class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # J = jumbo, S = small
        # 4J + 2S = tomatoSlices
        # J + S = cheeseSlices

        if tomatoSlices % 2 != 0:
            return []

        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo

        if jumbo < 0 or small < 0:
            return []

        return [jumbo, small]