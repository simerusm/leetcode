class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor: int) -> int:
            return sum((num + divisor - 1) // divisor for num in nums)
        
        l = 1
        r = max(nums)
      
        while l < r:
            divisor = (l + r) // 2
            if compute_sum(divisor) <= threshold:
                r = divisor
            else:
                l = divisor + 1
        
        return l
