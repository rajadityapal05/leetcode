class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        stones = sorted(
            zip(aliceValues, bobValues),
            key=lambda x: x[0] + x[1],
            reverse=True
        )

        alice = 0
        bob = 0

        for i, (a, b) in enumerate(stones):
            if i % 2 == 0:
                alice += a
            else:
                bob += b

        if alice > bob:
            return 1
        if alice < bob:
            return -1
        return 0