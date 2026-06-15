# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next==None:
            return None
        if not head.next.next:
            if n==1:
                head.next=None
            else:
                head=head.next
            return head
        nodes=[]
        cur=head
        while cur:
            nodes.append(cur)
            cur=cur.next
        if n==len(nodes):
            return head.next
        nodes[-(n+1)].next = nodes[-n].next
        return head
        