class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = 1
        prefix_sum = 1
        for num in nums:
            prefix_sum -= num
            min_value = max(min_value, prefix_sum)
        
        return min_value
