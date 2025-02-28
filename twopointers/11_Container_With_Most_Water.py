class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            # move the smallest one each time
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

"""
- Two pointer question
- While left pointer is smaller than right pointer perform logic,
  - Update the current result and check if we’ve hit a max
  - Remember to do r - l and not r - l + 1, we need the distance from one end to the other, non inclusive of one of the ends, usually we include both ends but in this case we don’t want to include one
  - Multiply the above by the minimum pillar
  - Then on every iteration keep the largest pillar each time and move the smaller one
- Time complexity: O(n) since we’re traversing the array and every element once
- Space complexity: O(1) since we’re not storing anything in a data structure
"""
