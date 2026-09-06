class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = {0: 1}

        odd = 0
        answer = 0

        for num in nums:

            if num % 2 == 1:
                odd += 1

            if odd - k in count:
                answer += count[odd - k]

            count[odd] = count.get(odd, 0) + 1

        return answer