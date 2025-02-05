class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr: List[int]) -> None:
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in nums:
                # make sure to prune unnecessary branches that have duplicates
                if i in curr: # O(1) since length of nums is at most 6
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop() # undo append
            return
        backtrack([])
        return res
