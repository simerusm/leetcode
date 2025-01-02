import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)

        for i in range(len(nums) - k):
            _ = heapq.heappop(min_heap)
        
        return min_heap[0]
