class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range(len(edges)+1)]
        rank=[1]*len(edges)
        def find(n):
            res=n
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        def union(n1,n2):
            u,v=find(n1),find(n2)
            if u==v:
                return False
            elif rank[u-1]<rank[v-1]:
                rank[v]+=1
                par[u]=v
            else:
                rank[u]+=1
                par[v]=u
            return True
        for i,j in edges:
            if not union(i,j):
                return [i,j]
        
