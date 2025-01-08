class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum([nums[i] for i in range(0, k)])
        max_average = current_sum / k

        left_pointer = 0
        for right_pointer in range(k, len(nums)):
            current_sum -= nums[left_pointer] - nums[right_pointer]
            max_average = max(max_average, current_sum / k)

            left_pointer += 1
        
        return max_average
