import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)

        cost = 0

        while len(min_heap) > 1:
            first_min = heapq.heappop(min_heap)
            second_min = heapq.heappop(min_heap)

            cost += first_min + second_min

            heapq.heappush(min_heap, first_min + second_min)
        
        return cost
