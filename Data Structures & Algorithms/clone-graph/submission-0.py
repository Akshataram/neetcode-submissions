"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone={}
        clone[node]=Node(node.val)
        q=deque([node])
        while q:
            a=q.popleft()
            for nei in a.neighbors:
                if nei not in clone:
                    clone[nei]=Node(nei.val)
                    q.append(nei)
                clone[a].neighbors.append(clone[nei])
        return clone[node]
