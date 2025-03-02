# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(node: TreeNode, numBuilder: str):
            if not node:
                return

            numBuilder += str(node.val)

            if node.left == None and node.right == None:
                nums.append(int(numBuilder))
                return
            
            left = dfs(node.left, numBuilder)
            right = dfs(node.right, numBuilder)
            return
        
        dfs(root, '')
        return sum(nums)

"""
- Do a DFS traversal
- In the dfs function
  - Pass in the node and a numBuilder string to keep track of the number at various points of the DFS as parameters
  - Check for the base case of Node not being a None type
  - On each node iteration update the numBuilder to include the current node’s value
  - Only append to the final num array if it’s a leaf node (left and right pointers are None)
- Do left and right dfs traversal
- Time complexity: O(n) because we’re visiting each node at most once
- Space complexity: O(h) where h is the max height of the binary tree due to the recursive call of the DFS, uses stack; worst case, the entire tree is lopsided and space complexity will be O(n)
"""
