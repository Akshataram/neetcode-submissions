# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=n
        temp=head
        cur=head
        while c>0:
            temp=temp.next
            c=c-1
        if temp is None:
            return head.next
        while temp:
            prev=cur
            temp=temp.next
            cur=cur.next
        prev.next=prev.next.next
        return head
        