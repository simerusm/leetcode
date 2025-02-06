class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()

        for l in range(len(nums)):
            m = l + 1
            r = len(nums) - 1
            while m < r:
                currSum = nums[l] + nums[m] + nums[r]
                if currSum == 0 and (nums[l], nums[m], nums[r]) not in seen:
                    res.append([nums[l], nums[m], nums[r]])
                    seen.add((nums[l], nums[m], nums[r]))
                elif currSum > 0:
                    r -= 1
                else:
                    m += 1
        return res
