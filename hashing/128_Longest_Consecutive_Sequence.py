class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            counter = 1
            # only start from the start of a seq to avoid duplicates
            if num - 1 not in nums:
                temp = num
                while temp + 1 in nums:
                    counter += 1
                    temp += 1
            res = max(res, counter)
        return res

"""
- Hashmap (set) type problem
- Make sure to iterate over the set and not the original array, the original array can contain many duplicates of the same starting number causing many unnecessary iterations
- Loop through the newly turned set and start the iteration of checking for the longest consecutive sequence if the current number - 1 doesn’t exist in the set
- Once a number like this is found, use a while loop to see how far you can go starting from that number, keep track of the value and update the result
- Time complexity: O(n), at most we’ll be visiting all the elements in the set array once, and access is O(1)
- Space complexity: O(n) worst case if nums contains all distinct elements thus it will be the same size as its set counterpart
"""
