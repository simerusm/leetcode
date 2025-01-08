class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest_subarray_len = float('-inf')
        
        zero_count = 0
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer] == 0:
                zero_count += 1

            while left_pointer <= right_pointer and zero_count > k:
                if nums[left_pointer] == 0:
                    zero_count -= 1
                left_pointer += 1

            longest_subarray_len = max(longest_subarray_len, right_pointer - left_pointer + 1)
        
        return longest_subarray_len
