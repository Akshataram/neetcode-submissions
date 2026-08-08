class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ones=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    ones+=1
        minutes=0
        while queue and ones:
            for i in range(len(queue)):
                a,b=queue.popleft()
                dr=[(-1,0),(0,1),(0,-1),(1,0)]
                for r,c in dr:
                    nr=a+r
                    nc=b+c
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        if grid[nr][nc]==1:
                            queue.append((nr,nc))
                            ones-=1
                            grid[nr][nc]=2
            minutes+=1
        return -1 if ones>0 else minutes
                        