# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        prev = None
        deleteNode = head
        pos = count - n
        while deleteNode and pos > 0:
            prev = deleteNode
            deleteNode = deleteNode.next
            pos -= 1
        if prev:
            prev.next = deleteNode.next
        else:
            head = deleteNode.next

        return head

"""
- The cleaner way to do this is by establishing 2 pointers left and right, make the right pointer n distance away from the left (which is at the start) and then iterate through the linked list until right is no longer a valid node to get the left pointer to be exactly at the destination you need
- You can also count the number of elements in the linked list first, then iterate to number of elements - n to find which node to skip over
  - Once found, just skip over it
- Edge case is when you need to delete the very first node (head), you need to make sure prev is not None, if it is then just set the head to be the node to be deleted’s next node
- Time complexity is O(n), we’re doing 2 passes so technically it should be O(2n) but it gets amortized to O(n)
- Space complexity is O(1), we’re not storing anything
"""
