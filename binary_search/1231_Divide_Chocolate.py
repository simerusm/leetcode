class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l = min(sweetness)
        r = sum(sweetness) // (k+1) # best case scenario is everyone receives equal amount
        ans = l
        
        while l <= r:
            m = (r + l) // 2

            # Greedily select sweetness for given pieces
            curr_sweetness = 0
            pieces = 0
            for ind, s in enumerate(sweetness):
                curr_sweetness += s
                if curr_sweetness >= m:
                    curr_sweetness = 0
                    pieces += 1
            
            if pieces >= k + 1:
                ans = max(m, ans)
                l = m + 1
            else:
                r = m - 1
        
        return ans

'''
- Binary search + greedy problem
- This is an optimization problem wherein you have to maximize the minimum, when you find a sweetness level that works you want to see if theres a larger sweetness level that works and move the binary search left pointer to the right
- If you find a sweetness level that doesn't work, then you're outside of the problem bounds, which means you have to move your right pointer to the left since nothing to the right of it would work
- The minimum value the sweetness could be is the minimum value in the array, if it was anything smaller than that like 0 then you would need to make an imaginary cut that doesn't split the array, resulting in infinite/no solutions
- The maximum value is the sum of all the sweetness elements divided by the number of pieces you need (k+1), in the most ideal scenario everyone would have an equal amount of sweetness which maximizes the minimum, vertex of a positive quadratic function
- Time Complexity: O(nlogn)
- Space Complexity: O(1)
'''
