# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        queue=deque([root])
        while queue:
            for i in range(len(queue)):
                q1=queue.popleft()
                if q1.left:
                    queue.append(q1.left)
                if q1.right:
                    queue.append(q1.right)
            res.append(q1.val)
        return res
            