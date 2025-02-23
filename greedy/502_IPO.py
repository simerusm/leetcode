import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        i = 0
        heap = [] # max heap

        for _ in range(k):
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                return w
            
            w -= heapq.heappop(heap)
        
        return w

"""
- greedy algo problem
- we need to ensure that we're choosing the max profitable project with the given capital we have at a moment in time, so greedily choose the max profits that our current capital can get whenever we have a choice 
- package the capital and profits into an array and have it in sorted order, we have it in ascending order to make sure that we're able to even make profits in the initial projects
- wrap all the logic in a for loop that runs only k number of times
- inside the for loop, in every iteration (a snapshot of time where we have a certain capital), use a while loop to add as many projects as we can that satisfy the capital budget at that snapshot of time to our max heap
    - make sure to negate all the elements when adding to turn min heap to max heap
- in a for loop iteration, after we try and add all the projects to our heap, if there's none we can add then we return the capital we have amassed at that moment in time beacuse there will not be any more projects that are going to satisfy our constraints because it's in sorted order
- for every iteration, make sure you add the highest profit we can get at that moment in time to make use of our greedy strategy to amass the most capital
- Time Complexity: O((k + n)logn + nlogn) --> O((k + n)logn) where n is the number of projects given. The heap's max size is n, which means its operations are logn in the worst case, and we do k + n operations (k pop operations, n push operations)
- Space Complexity: O(n) due to the heap in the worst case
"""
