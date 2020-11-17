# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = q = worker = ListNode()
        root = worker
        p, q = l1, l2
        carry = 0        
        while(p != None or q != None or carry):                
            x = p.val if p else 0
            p = p.next if p else None
            y = q.val if q else 0
            q = q.next if q else None
            carry, curval = divmod(x + y + carry, 10)           
            nextNode = ListNode(curval)
            worker.next = nextNode
            worker = worker.next
        return root.next
