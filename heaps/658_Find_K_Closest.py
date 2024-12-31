import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            abs_diff_and_num = (-abs(num - x), -num)
            heapq.heappush(max_heap, abs_diff_and_num)

            if len(max_heap) > k:
                _ = heapq.heappop(max_heap)
        
        closest_nums = [-num for abs_val, num in max_heap]
        closest_nums.sort()

        return closest_nums
