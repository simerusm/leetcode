import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap: list[int] = []
        self.min_heap: list[int] = []

    def addNum(self, num: int) -> None:
        # l = [-2, -1], max heap
        # r = [3, 4], min heap
        # actual representation --> [?, 2, 3, ?]
        heapq.heappush(self.max_heap, -num)
        max_of_left = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_of_left)

        if len(self.max_heap) < len(self.min_heap):
            min_of_right = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_of_right)

    def findMedian(self) -> float:
        max_of_left = -self.max_heap[0]
        
        if len(self.max_heap) == len(self.min_heap):
            min_of_right = self.min_heap[0]
            return (max_of_left + min_of_right) / 2

        return max_of_left


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
