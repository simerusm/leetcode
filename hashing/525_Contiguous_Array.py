class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr_sum = 0
        max_length = 0

        diff_to_index = {}

        for idx, num in enumerate(nums):
            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            
            if curr_sum not in diff_to_index:
                diff_to_index[curr_sum] = idx
            
            if curr_sum == 0:
                max_length = idx + 1
            else:
                max_length = max(max_length, idx - diff_to_index[curr_sum])
        
        return max_length
