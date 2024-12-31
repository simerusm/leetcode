import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        min_heap = []

        for num, freq in frequency_map.items():
            curr = (freq, num)
            heapq.heappush(min_heap, curr)
            
            if len(min_heap) > k:
                _ = heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]
