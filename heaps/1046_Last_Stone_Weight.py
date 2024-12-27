class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        # convert items to negative to turn into a max heap
        stones = [-i for i in stones]

        # heapify the stones list --> max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            # pop the max element
            y = heapq.heappop(stones)

            # pop 2nd most max element
            x = heapq.heappop(stones)

            # case 1
            if y == x:
                continue
            
            # case 2
            heapq.heappush(stones, y - x)
        
        # check for edge case, all stones are destroyed
        if stones:
            return -stones[0]
        else:
            return 0

        '''
        TC: O(n + nlogn) --> O(nlogn)
        SC: O(n) --> note that since we're reusing the input, the input array counts towards Space Complexity
        '''
