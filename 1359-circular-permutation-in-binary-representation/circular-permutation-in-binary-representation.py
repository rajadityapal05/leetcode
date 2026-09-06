class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        answer = []

        for i in range(1 << n):
            gray = i ^ (i >> 1)
            answer.append(gray ^ start)

        return answer