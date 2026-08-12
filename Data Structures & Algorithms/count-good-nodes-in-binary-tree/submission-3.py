# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        c=0
        queue=deque([(root,root.val)])
        while queue:
            a,b=queue.popleft()
            if a.left:
                if a.left.val<b:
                    queue.append((a.left,b))
                else:
                    c+=1
                    queue.append((a.left,a.left.val))
            if a.right:
                if a.right.val<b:
                    queue.append((a.right,b))
                else:
                    c+=1
                    queue.append((a.right,a.right.val))
        return c+1

