# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head

        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
            curr = curr.next

        # edge cases for when there's duplicates at the end
        if prev:
            prev.next = curr
        
        return head
