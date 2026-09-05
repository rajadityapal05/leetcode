import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:

        if val in self.index:
            return False

        self.index[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val not in self.index:
            return False

        index = self.index[val]
        last = self.nums[-1]

        self.nums[index] = last
        self.index[last] = index

        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.nums)