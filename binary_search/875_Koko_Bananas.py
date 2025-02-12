class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeNeededForANum(num: int) -> int:
            timeNeeded = 0
            for i in piles:
                # perform ceiling division
                timeNeeded += (i + num - 1) // num
            return timeNeeded

        l = 1
        r = max(piles)
        lastMinTime = float('inf')

        while l <= r:
            k = (l + r) // 2 # bananas-per-hour eating speed
            timeNeeded = timeNeededForANum(k) 

            if timeNeeded <= h:
                lastMinTime = min(lastMinTime, k)
                r = k - 1
            else:
                l = k + 1

        return lastMinTime
