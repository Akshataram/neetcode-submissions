# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack=[[p,q]]
        while stack:
            a,b=stack.pop()

            if a.val==b.val:
                if a.left and b.left:
                    stack.append([a.left,b.left])
                elif a.left or b.left:
                    return False
                else:
                    pass
                if a.right and b.right:
                    stack.append([a.right,b.right])
                elif a.right or b.right:
                    return False
                else:
                    pass
            else:
                return False
        return True    

