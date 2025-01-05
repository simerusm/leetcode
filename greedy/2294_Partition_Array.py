class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsequences = 1
        currMin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - currMin > k:
                currMin = nums[i]
                subsequences += 1
        
        return subsequences
