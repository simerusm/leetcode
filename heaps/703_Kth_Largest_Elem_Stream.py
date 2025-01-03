import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        self.min_heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
            
        # Only add if val to add is bigger than the kth largest element currently
        elif self.min_heap[0] < val:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0]
