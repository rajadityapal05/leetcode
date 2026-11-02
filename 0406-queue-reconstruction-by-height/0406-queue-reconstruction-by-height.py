class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))

        queue = []

        for person in people:
            queue.insert(person[1], person)

        return queue