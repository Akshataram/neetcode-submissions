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
        max1=root.val
        queue=deque([(root,max1)])
        c=1
        while queue:
            a,maxi=queue.popleft()
            if a.left:
                if maxi<=a.left.val:
                    c+=1
                    queue.append((a.left,a.left.val))
                else:
                    queue.append((a.left,maxi))
            if a.right:
                if maxi<=a.right.val:
                    c+=1
                    queue.append((a.right,a.right.val))
                else:
                    queue.append((a.right,maxi))
        return c