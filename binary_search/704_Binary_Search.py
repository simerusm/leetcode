class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

"""
Side notes:
- In C++ you would need to worry about overflow when you calculate the midpoint
- When you do (l + r) / 2, since integers have a fixed size in a compiled language, this could result in integer overflow wherein you get a number larger than what it's expecting to handle
- Thats why in a compiled language where the size of a number is finite, you need to do l + (r - l) / 2, wherein you calculcate the r - l / 2 (gauranteed to be below the limit) and then add l to it
- In python, we don't have to worry about this because Python uses arbitrary-precision integers, wherein the size of the integer isn't fixed. 
- Python allocates as much memory as needed to store the value, so it can grow to any size which is why it's safe to do l + r / 2 without worrying about overflow occuring

- Regular binary search
- Time Complexity: O(logn)
- Space Complexity: O(1)
"""
