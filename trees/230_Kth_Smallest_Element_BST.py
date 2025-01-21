# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        curr_k = k
        res = None

        def inOrder(node: Optional[TreeNode]) -> None:
            nonlocal curr_k, res

            if not node or res:
                return
            
            inOrder(node.left)
            curr_k -= 1
            if curr_k == 0:
                res = node.val
                return
            inOrder(node.right)
        
        inOrder(root)
        return res
