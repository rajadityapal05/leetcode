import random

class Solution:

    def __init__(self, nums: List[int]):
        self.index = {}

        for i in range(len(nums)):
            if nums[i] not in self.index:
                self.index[nums[i]] = []

            self.index[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index[target])