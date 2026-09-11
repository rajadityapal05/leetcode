import random


class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.bound = n - len(blacklist)
        self.mapping = {}

        blacklist_set = set(blacklist)

        # Valid numbers available in the upper range
        last = n - 1

        for b in blacklist:
            # Only remap blacklisted numbers inside [0, bound - 1]
            if b < self.bound:

                # Find a valid number from the upper range
                while last in blacklist_set:
                    last -= 1

                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        x = random.randrange(self.bound)

        if x in self.mapping:
            return self.mapping[x]

        return x