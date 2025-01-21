# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node: Optional[TreeNode], currDepth: int = 0) -> None:
            nonlocal depth
            if not node:
                depth = max(currDepth, depth)
                return
            
            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)
        
        dfs(root)
        return depth
