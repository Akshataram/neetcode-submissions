class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        visited=set()
        count=0
        for i,v in edges:
            adj[i].append(v)
            adj[v].append(i)
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                dfs(i)
        return count


        
