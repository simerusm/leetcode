# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            ans += self.rangeSumBST(root.right, low, high)
        
        return ans

"""
- Can solve this using DFS and BFS as well, in this I used BST to solve
- Recurse through it, have if statements checking for if the current node value is lower or higher or equal to the boundaries and then based off that recurse down lower/higher 
- We return the current sum of all the nodes below and include the current as the answer
- Time Complexity: O(n), we visit every node to check its value
- Space Complexityy: O(n), worst case we have a linked-list tree thus creating n stack frames where n is the height of the tree
"""
