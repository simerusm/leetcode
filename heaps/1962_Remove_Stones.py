import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            max_pile = -heapq.heappop(piles)
            max_pile = math.ceil(max_pile / 2)

            heapq.heappush(piles, -max_pile)

        return -sum(piles)
