# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            r=[]
            for i in range(len(queue)):
                q1=queue.popleft()
                r.append(q1.val)
                if q1.left:
                    queue.append(q1.left)
                if q1.right:
                    queue.append(q1.right)
            ans.append(r)
        return ans