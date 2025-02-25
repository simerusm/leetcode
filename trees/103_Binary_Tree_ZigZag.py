# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []

        if not root:
            return []

        direction = "right"
        q = deque([root])

        while q:
            length = len(q)

            temp = []
            if direction == "right":
                for ind in range(length):
                    temp.append(q[ind].val)
                direction = "left"
            else:
                for ind in range(length - 1, -1, -1):
                    temp.append(q[ind].val)
                direction = "right"
            res.append(temp)

            for _ in range(length):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return res

"""
- BFS problem
- Carry out normal BFS and then keep track of which direction you need to get the current level at
- If its right, use a for loop to iterate through the current queue (BEFORE YOU START POPPING) and add every value of the TreeNode to a temp array and then once thats done add it a result array
- If its left iterate through the current queue in reverse and then do the same thing
- Regular BFS popping logic off the queue once checks are done
- Time complexity: O(n) since we visit each element once and the intermediary for loops to append values of the binary tree nodes to the temp array are ammortized
- Space complexity: O(n), the queue can hold up to O(w) nodes at a time, where w is the maximum width of the tree. In the worst case, w can be n/2, which is still O(n)
"""
