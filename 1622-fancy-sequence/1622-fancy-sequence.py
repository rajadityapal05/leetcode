class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []

        # Current transformation:
        # value = original * mul + add
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        # Store the value in its original form,
        # undoing the current global transformation.
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)

        original = (val - self.add) % self.MOD
        original = original * inv_mul % self.MOD

        self.seq.append(original)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1

        return (self.seq[idx] * self.mul + self.add) % self.MOD