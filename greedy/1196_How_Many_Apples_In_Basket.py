class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        LIMIT = 5000

        weight.sort()
        curr_sum = 0
        counter = 0
        for w in weight:
            if curr_sum + w <= LIMIT:
                counter += 1
                curr_sum += w
            else:
                break
        return counter

"""
- Greedy problem with sorting solution
- Sort it in ascending order since we want to maximize for the number of apples, not the weight
- Iterate through the list and see if we can add the current apple to our running sum, if not then break and then return the apples we counted
- Time Complexity: O(nlogn) due to sorting
- Space Complexity: O(1) by leetcode standards but Timsort takes O(n) space under the hood
"""
