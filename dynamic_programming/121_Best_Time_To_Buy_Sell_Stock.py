class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        res = 0
        for price in prices:
            lowest = min(lowest, price)
            res = max(res, price - lowest)
        return res

"""
- Simple sliding window problem wherein we take into account every single option and brute force our answer (thats where the dp part comes into play)
- Have a pointer that keeps track of the lowest number you’ve iterated over
- Iterate through all elements in array, updating the lowest if you find a lower value and then calculating the profit rom the current price to the lowest and making sure you return the max
- Time complexity: O(n), we iterate through the array once and visit all elements once
- Space complexity: O(1), we’re not storing anything
"""
