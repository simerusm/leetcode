class Solution:
    def halveArray(self, nums: List[int]) -> int:
        import heapq

        # turn the nums list into a max heap
        nums = [-i for i in nums]
        heapq.heapify(nums)

        res = 0
        currSum = -sum(nums)
        target = currSum / 2

        # find min num of divisions
        while currSum > target:
            # pop largest num, remove that from currSum
            curr = -heapq.heappop(nums)
            currSum -= curr

            # divide curr popped item by half
            curr /= 2

            # add back to the heap as a negative number and update currSum
            heapq.heappush(nums, -curr)
            currSum += curr

            # +1 operation
            res += 1
        
        return res

        '''
        TC: O(n + nlogn) --> O(nlogn)
        SC: O(n)
        '''
