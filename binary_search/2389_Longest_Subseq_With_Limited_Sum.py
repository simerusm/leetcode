class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort() # O(nlogn)

        prefix_sum = []
        curr_sum = 0
        for i in range(len(nums)): # O(n)
            curr_sum += nums[i]
            prefix_sum.append(curr_sum)

        def binary_search(max: int) -> int:
            l = 0
            r = len(prefix_sum) - 1
            while l <= r:
                m = (l + r) // 2
                if prefix_sum[m] == max:
                    return m + 1
                elif prefix_sum[m] > max:
                    r = m - 1
                else:
                    l = m + 1
            return r + 1
        
        for q in queries: # O(mlogn)
            res.append(binary_search(q))
        
        return res

"""
- Binary search problem
- Sort the nums array and then caluclate the prefix sum so that we can do binary search on it
  - Note that we're finding the longest subsequence array, so the array we find can involve elements out of order from the original array that was provided
- For every query in the queries array do binary search on the prefix sum array to find the longest possible sum
  - Make sure to return the right pointer if we don't find a perfect match
  - The left pointer tells us where the max value would go if we were to insert it in sorted position, however, in this case right tells us that the max index from the start 
- Time Complexity: O(nlogn) + O(n) + O(mlogn) = O(nlogn) + O(mlogn), comments added in the code for clarity, m is the length of queries array and n is the length of nums array
- Space Complexity: O(n) since we're storing n elements in prefix_sum array
"""
