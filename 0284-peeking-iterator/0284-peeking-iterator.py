class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = False
        self.next_element = None

    def peek(self) -> int:
        if not self.peeked:
            self.next_element = self.iterator.next()
            self.peeked = True

        return self.next_element

    def next(self) -> int:
        if self.peeked:
            self.peeked = False
            return self.next_element

        return self.iterator.next()

    def hasNext(self) -> bool:
        return self.peeked or self.iterator.hasNext() 