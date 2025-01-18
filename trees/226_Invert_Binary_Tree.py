# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: Optional[TreeNode]) -> None:
            if not node:
                return

            left_node_next = node.left
            node.left = node.right
            node.right = left_node_next
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
            
        invert(root)
        return root
