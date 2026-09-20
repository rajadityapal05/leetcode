class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        count = {0: 1}
        total = {0: 0}

        prefix = 0
        answer = 0

        for k, num in enumerate(arr):
            prefix ^= num

            if prefix in count:
                answer += count[prefix] * k - total[prefix]

            count[prefix] = count.get(prefix, 0) + 1
            total[prefix] = total.get(prefix, 0) + k + 1

        return answer