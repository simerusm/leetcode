class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        def backtrack(curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            for i in nums:
                # prune duplicate branches
                if i in curr:
                    continue

                if curr == [] or (curr and curr[-1] < i):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return res

"""
- Backtracking problem similar to subsets down below
- Create the list from 1 to n
- In the backtracking function make sure to set the base case to be once we reach length curr equal to k
  - Also in the base case, add it to the res array
- In each stack call loop through the possible numbers , make sure to prune branches that satisfy invalid conditions and also avoid duplicate arrays e.g. [1, 2] and [2, 1] by making sure it only increases in magnitude
- Time complexity: Combination formula n! / (r! * (n - r)!) because we're literally just getting all the possible combinations
- Space complexity: O(k), the recursion stack will go to a max depth of k due to the base condition we imposed
"""
