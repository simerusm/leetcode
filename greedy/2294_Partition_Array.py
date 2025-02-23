class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_min = nums[0]
        subsequences = 1

        for i in range(1, len(nums)):
            if nums[i] - curr_min <= k:
                continue
            curr_min = nums[i]
            subsequences += 1
        
        return subsequences

"""
- greedy problem
- we need to make sure we're sorting the array to find the minimum number of subsequences
    - note that the max would be just the length of the array, if we were to partition at every element index
- important note about subsequnces and sorting
    - the problem asks you to partition the array into subsequences. this means you need to divide the elements into groups (subsequences) that meet the difference constraint.
    - the problem does not require you to find subsequences that exist in the original, unsorted array.
- we need to build up the subsequence up until the condition is broken (max - min is at most k)
- once the condition gets broken, begin a new subsequnce at that element the previous subsequence breaks, make sure to make this new element the new current subsequence min, because the array is in sorted order, at the start of a new "subsequence" 
- time complexity: O(nlogn + n) --> O(nlogn), because we sort and loop through the array but it gets ammortized to just O(nlogn)
- space complexity: O(n), timsort (python's implementation of .sort()) uses up to O(n) space
"""
