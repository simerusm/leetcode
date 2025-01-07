class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_ptr = 0
        right_ptr = len(nums) - 1

        place_ptr = len(nums) - 1
        squared_nums = [0 for i in range(len(nums))]

        nums = [num ** 2 for num in nums]

        while left_ptr <= right_ptr:
            if nums[left_ptr] > nums[right_ptr]:
                squared_nums[place_ptr] = nums[left_ptr]
                left_ptr += 1
            else:
                squared_nums[place_ptr] = nums[right_ptr]
                right_ptr -= 1
            
            place_ptr -= 1
        
        return squared_nums
