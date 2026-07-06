class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[-1]*n
        maxp=0
        def dfs(i):
            if i<=0:
                if i==0:
                    return nums[i]
                else:
                    return 0
            if cache[i]!=-1:
                return cache[i]
            maxp=max((nums[i]+dfs(i-2)),dfs(i-1))
            cache[i]=maxp
            return maxp
        return dfs(n-1)