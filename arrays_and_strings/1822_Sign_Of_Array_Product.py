class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_counter = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative_counter += 1
        
        if negative_counter % 2 == 0:
            return 1
        return -1
