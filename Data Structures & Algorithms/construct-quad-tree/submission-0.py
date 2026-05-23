"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid[0])
        def dfs(si,ei,sj,ej):
            c=grid[si][sj]
            flag=True
            for i in range(si,ei):
                for j in range(sj,ej):
                    if grid[i][j]==c:
                        pass
                    else:
                        flag =False
                        break
            if flag:
                return Node(c,1)
            else:
                val = 1
                isLeaf = 0
                mr=(si+ei)//2
                ms=(sj+ej)//2
                topLeft = dfs(si, mr, sj, ms)
                topRight = dfs(si, mr, ms, ej)
                bottomLeft = dfs(mr, ei, sj, ms)
                bottomRight = dfs(mr, ei, ms, ej)
            return Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight)
        return dfs(0,n,0,n)


