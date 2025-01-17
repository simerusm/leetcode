# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node: TreeNode, currMax: int) -> None:
            nonlocal count

            if not node:
                return
            
            if node.val >= currMax:
                count += 1
                currMax = node.val
            
            if node.left:
                dfs(node.left, currMax)
            if node.right:
                dfs(node.right, currMax)
            
            return
        
        dfs(root, float('-inf'))
        return count
