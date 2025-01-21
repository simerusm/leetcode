# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def treeHeight(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter

            if not node:
                return 0
            
            left = treeHeight(node.left)
            right = treeHeight(node.right)
            max_diameter = max(max_diameter, left + right)

            return max(left + 1, right + 1)

        treeHeight(root)
        return max_diameter
