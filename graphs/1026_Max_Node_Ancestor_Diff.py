# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, minVal, maxVal):
            # base case
            if not curr:
                return abs(maxVal - minVal)
            
            # dfs down left and right branch and keep track of min and max values until you reach bot
            # once you're at bottom, return the difference between max and min
            # for that particular branch, that's the biggest difference you'll get, 
            # then compare with other branches
            left = dfs(curr.left, min(minVal, curr.val), max(maxVal, curr.val))
            right = dfs(curr.right, min(minVal, curr.val), max(maxVal, curr.val))
            
            return max(left, right)
            
        return dfs(root, root.val, root.val)

"""
- Use recursion to solve this graph problem
- Basically do dfs and go down every single route and try and find the biggest difference down every single route
- Then compare all these differences with each route and return the biggest one
- Create a new local function that takes max and min values as parameters as well, use this to keep track of what the max and min values of the ancestor nodes are at a specific node 
"""
