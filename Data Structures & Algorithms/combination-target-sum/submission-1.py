class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(index,path):
            for i in range(index,len(nums)):
                num=nums[i]
                if num+sum(path[:])>target:
                    continue
                path.append(num)
                if sum(path[:])==target:
                    res.append(path[:])
                else:
                    backtrack(i,path)
                path.pop()
        backtrack(0,[])
        return res
                    