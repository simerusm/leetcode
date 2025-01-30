if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        if not list2 and not list1:
            return None
        
        l1Node = list1
        l2Node = list2

        res = ListNode(0)
        curr = res
        while l1Node and l2Node:
            if l1Node.val > l2Node.val:
                curr.next = l2Node
                curr = curr.next
                l2Node = l2Node.next
            else:
                curr.next = l1Node
                curr = curr.next
                l1Node = l1Node.next
        
        if l1Node:
            curr.next = l1Node
        if l2Node:
            curr.next = l2Node

        return res.next
