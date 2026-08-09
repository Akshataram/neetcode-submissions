class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank=[1]*n
        def find(n):
            res=n
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        def union(n1,n2):
            u,v=find(n1),find(n2)
            if u==v:
                return 0
            if rank[u]>rank[v]:
                rank[u]+=1
                par[v]=u
            else:
                rank[v]+=1
                par[u]=v
            return 1
        res=n
        for i,v in edges:
            res-=union(i,v)
        return res
            

