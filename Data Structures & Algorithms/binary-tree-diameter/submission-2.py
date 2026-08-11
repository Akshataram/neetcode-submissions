# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def maxdepth(node):
            if not node:
                return 0
            self.d=max(self.d,maxdepth(node.left)+ maxdepth(node.right))
            return 1+max(maxdepth(node.left),maxdepth(node.right))
        maxdepth(root)
        return self.d