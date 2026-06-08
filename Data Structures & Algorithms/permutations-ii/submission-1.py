class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[0]*len(nums)
        nums.sort()
        def backtrack(used,path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i]=1
                backtrack(used,path)
                used[i]=0
                path.pop()
        backtrack(used,[])
        return res
