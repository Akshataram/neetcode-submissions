class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return
            if (i,j) in visited:
                return
            else:
                visited.add((i,j))
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        visited=set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0':
                    continue
                if (i,j) in visited:
                    continue
                else:
                    count+=1
                    visited.add((i,j))
                    dfs(i+1,j)
                    dfs(i,j+1)
                    dfs(i-1,j)
                    dfs(i,j-1)
        return count
                