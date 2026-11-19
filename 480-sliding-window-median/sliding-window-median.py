
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        small = []  # Max heap (negative values)
        large = []  # Min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune(heap, is_small):
            while heap:
                num = -heap[0] if is_small else heap[0]

                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                prune(small, True)
                num = -heapq.heappop(small)
                heapq.heappush(large, num)
                small_size -= 1
                large_size += 1
                prune(small, True)

            elif small_size < large_size:
                prune(large, False)
                num = heapq.heappop(large)
                heapq.heappush(small, -num)
                large_size -= 1
                small_size += 1
                prune(large, False)

        def add_num(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            rebalance()

        def remove_num(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1

                if num == -small[0]:
                    prune(small, True)
            else:
                large_size -= 1

                if large and num == large[0]:
                    prune(large, False)

            rebalance()

        def get_median():
            prune(small, True)
            prune(large, False)

            if k % 2:
                return float(-small[0])

            return (-small[0] + large[0]) / 2.0

        result = []

        # Build the first window
        for i in range(k):
            add_num(nums[i])

        result.append(get_median())

        # Slide the window
        for i in range(k, len(nums)):
            remove_num(nums[i - k])
            add_num(nums[i])
            result.append(get_median())

        return result
