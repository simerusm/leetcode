class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        
        l = max(nums)
        r = sum(nums)
        ans = float('inf')
        
        # binary search on bounds and greedily separate into subarrays
        while l <= r:
            m = (l + r) // 2
            
            curr_sum = 0
            splits = 0
            for n in nums:
                if curr_sum + n <= m:
                    curr_sum += n
                else:
                    splits += 1
                    curr_sum = n
            
            if splits + 1 <= k:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        
        return ans


'''
- Binary search + greedy problem
- This is a minimization of the maximum problem. Whenever you find a viable solution, you then want to see if you can make it smaller by moving the right pointer to the left
- Within the greedy-based for loop inside each binary search run we must ensure that there's no excess in each partition of the array and must keep each partition bound to the m that the current binary search iteration is on
- If we find a value that doesn't work then we move the search space to the right since only the values that result in too many partitions need to be pruned until we find the minimum number that maximizes partitions
- Time Complexity: O(nlogn)
- Space Complexity: O(1)
'''
