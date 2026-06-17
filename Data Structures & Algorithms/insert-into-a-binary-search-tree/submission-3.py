# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root=TreeNode(val)
            return root
        cur=root
        while cur:
            if val>cur.val:
                prev=cur
                cur=cur.right
            elif val<cur.val:
                prev=cur
                cur=cur.left
        cur=TreeNode(val)
        if prev.val>cur.val:
            prev.left=cur
        else:
            prev.right=cur
        return root
