class Solution:
    def tribonacci(self, n: int) -> int:
        cache=[-1]*(n+1)
        if n <= 2:
            return 1 if n != 0 else 0
        cache[0],cache[1],cache[2]=0,1,1
        def dfs(i):
            if cache[i]!=-1:
                return cache[i]
            cache[i]=dfs(i-1)+dfs(i-2)+dfs(i-3)
            return cache[i]
        return dfs(n)