# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

# ------------------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_nodes = []
        q_nodes = []
        
        def dfs(node: Optional[TreeNode], node_list: List[Optional[TreeNode]]) -> None:
            if not node:
                node_list.append(None)
                return
            
            node_list.append(node.val)
            dfs(node.left, node_list)
            dfs(node.right, node_list)
        
        dfs(p, p_nodes)
        dfs(q, q_nodes)

        return p_nodes == q_nodes
