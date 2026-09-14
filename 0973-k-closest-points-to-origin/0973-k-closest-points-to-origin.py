import heapq


class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            distance = x * x + y * y

            # Max-heap simulation using negative distance
            heapq.heappush(heap, (-distance, x, y))

            # Keep only k closest points
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]