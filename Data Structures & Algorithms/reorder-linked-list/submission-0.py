# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        curr = head

        while curr and curr.next:

            # Find tail and node before tail
            tail = curr
            bfr = None

            while tail.next:
                bfr = tail
                tail = tail.next

            # Stop when pointers meet/cross
            if curr == tail or curr.next == tail:
                break

            temp = curr.next

            curr.next = tail
            tail.next = temp

            bfr.next = None

            curr = temp





