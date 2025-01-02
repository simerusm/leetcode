import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            point_distance_from_origin = (-math.sqrt(x**2 + y**2), (x, y))
            heapq.heappush(max_heap, point_distance_from_origin)

            if len(max_heap) > k:
                _ = heapq.heappop(max_heap)
        
        return [point for magnitude, point in max_heap]
