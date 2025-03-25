class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]

        def determineHours(speed: int) -> int:
            hours_needed = 0
            for bananas in piles:
                hours_needed += (bananas // speed) + (0 if bananas % speed == 0 else 1)
            return hours_needed

        res = float('inf')

        while l <= r:
            m = (l + r) // 2
            hours_needed = determineHours(m)

            if hours_needed == h:
                res = min(m, res)
            
            if hours_needed <= h:
                r = m - 1
            else:
                l = m + 1
        
        return min(l, res)

"""
- Binary search problem
- Instead of doing a binary search directly on the indices of the array given, we do a binary search on the constraints of the hours
    - We know that the minimum hours is going to be between 1 and the max element of the piles array
    - We can perform a binary search from 1 - max element of the array to find the minimum speed
- Note that whenever we calculate a midpoint, we need to determine how many hours it will take to complete all the bananas at that speed, perform a ceiling operation when adding stuff up
- In the actual binary search, if we find a speed that results in us being able to eat all the bananas in k hours, there could still potentially be a smaller speed
    - So, instead of returning the midpoint as soon as we reach the condition of hours, keep track of the minimum of all the computed values instead, getting as close to h as possible
    - In case we can't find anything that gets us to h exactly, we return the left pointer at the end
        - When l > r, l points to the smallest value that is greater than the last r value that resulted in hours_needed == h
        - This means that the left pointer is pointing to the smallest valid speed
        - If there was a value that resulted in hours_needed == h, then the res variable would contain that value (which will be smaller than the l value since it already crossed r)
        - At the end, we essentially are saying, when l > r, if r isn't valid, then l is valid
- Time Complexity: O(nlogn)
- Space Complexity: O(1)
"""
