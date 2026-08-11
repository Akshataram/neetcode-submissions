# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=True
        def maxdepth(node):
            nonlocal flag
            if not node:
                return 0
            if abs(maxdepth(node.left)- maxdepth(node.right))>1:
                flag=False
            return 1+max(maxdepth(node.left),maxdepth(node.right))
        maxdepth(root)
        return flag
