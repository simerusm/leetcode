class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                return
            
            res.append(curr.copy())
            for i in nums:
                if i in curr:
                    continue
                if (curr and curr[-1] < i) or curr == []:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
            return
        
        backtrack([])
        res.append(nums)
        return res
