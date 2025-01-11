class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        k_radius_averages = [-1 for i in range(len(nums))]

        prefix_sum = []
        accumulation = 0
        for num in nums:
            accumulation += num
            prefix_sum.append(accumulation)

        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                curr_radius_sum = prefix_sum[i + k]
                if i - k - 1 >= 0:
                    curr_radius_sum -= prefix_sum[i - k - 1]
                k_radius_averages[i] = curr_radius_sum // (k*2 + 1)
        
        return k_radius_averages
