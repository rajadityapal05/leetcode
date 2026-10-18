from typing import List
from bisect import bisect_right

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        votes = {}
        leader = -1
        max_votes = 0

        for person in persons:
            votes[person] = votes.get(person, 0) + 1

            if votes[person] >= max_votes:
                max_votes = votes[person]
                leader = person

            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t) - 1
        return self.leaders[index] 