class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_array = []
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            running_array.append(prefix_sum)
        
        return running_array
