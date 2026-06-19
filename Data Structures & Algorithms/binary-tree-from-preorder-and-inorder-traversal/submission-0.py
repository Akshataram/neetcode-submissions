# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d=defaultdict(int)
        for i,val in enumerate(inorder):
            d[val]=i
        k=0
        def build(l,r):
            nonlocal k
            if l > r:
                return None
            a=preorder[k]
            root=TreeNode(a)
            k+=1
            mid=d[a]
            root.left=build(l,mid-1)
            root.right=build(mid+1,r)
            return root
        return build(0,len(inorder)-1)

