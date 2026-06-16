# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        i=left
        pre,prev1=None,None
        while(i>1):
            pre=cur
            cur=cur.next
            i-=1
        prev=None
        j=right
        while (j-left)>=0:
            if j==right:
                prev1=cur
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            j-=1
        if not pre:
            head=prev
        else:
            pre.next=prev
        if not prev1:
            return head
        else:
            prev1.next=cur
            return head


