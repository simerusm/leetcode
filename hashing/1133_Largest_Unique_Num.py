from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_number = -1
        num_frequency = Counter(nums)
        for key, val in num_frequency.items():
            if val == 1:
                max_number = max(max_number, key)
        
        return max_number
