class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        cache=[[-1]* 2 for _ in range(n)]
        def dfs(i,flag):
            if i>=len(nums) or i==len(nums)-1 and flag==True:
                return 0
            if cache[i][flag]!=-1:
                return cache[i][flag]
            maxp=max(dfs(i+1,flag),nums[i]+dfs(i+2,flag))
            cache[i][flag]=maxp
            return maxp
        return max(dfs(0,True),dfs(1,False))


