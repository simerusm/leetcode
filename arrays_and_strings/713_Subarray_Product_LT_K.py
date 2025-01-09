class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        subarray_num = 0
        window_prod = 1
        l_ptr = 0
        for r_ptr in range(len(nums)):
            window_prod *= nums[r_ptr]
            while l_ptr <= r_ptr and window_prod >= k:
                window_prod //= nums[l_ptr]
                l_ptr += 1
            
            subarray_num += r_ptr - l_ptr + 1
        
        return subarray_num
