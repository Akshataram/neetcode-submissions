# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue=deque([(root,float("-inf"),float("inf"))])
        while queue:
            a,b,c=queue.popleft()
            if not (b<a.val<c):
                return False
            if a.left:
                queue.append((a.left,b,a.val))
            if a.right:
                queue.append((a.right,a.val,c))
        return True
