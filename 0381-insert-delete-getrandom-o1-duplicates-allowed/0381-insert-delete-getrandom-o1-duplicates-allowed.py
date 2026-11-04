import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:

        if val not in self.index:
            self.index[val] = set()

        self.index[val].add(len(self.nums))
        self.nums.append(val)

        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:

        if val not in self.index:
            return False

        remove_index = self.index[val].pop()

        last_index = len(self.nums) - 1
        last_value = self.nums[last_index]

        # If we're not removing the last element,
        # move the last element into its position.
        if remove_index != last_index:

            self.nums[remove_index] = last_value

            self.index[last_value].remove(last_index)
            self.index[last_value].add(remove_index)

        self.nums.pop()

        # Remove the value completely if no copies remain.
        if not self.index[val]:
            del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)