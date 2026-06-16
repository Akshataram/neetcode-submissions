# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=l1
        c,p=0,0
        while cur:
            c+=cur.val*(10**p)
            p+=1
            cur=cur.next
        cur=l2
        d,p=0,0
        while cur:
            d+=cur.val*(10**p)
            p+=1
            cur=cur.next
        n=c+d
        dummy=node=ListNode()
        if n==0:
            node.next=ListNode()
            return dummy.next
        while n>0:
            r=n%10
            n=n//10
            node.next=ListNode(r)
            node=node.next
        return dummy.next


