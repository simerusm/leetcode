class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        curr = 0
        while curr in nums:
            curr += 1
        return curr
