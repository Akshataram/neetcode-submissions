class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result=0
        def backtrack(index,path):
            nonlocal result
            if index==len(nums):
                xorr=0
                for i in path[:]:
                    xorr^=i
                result+=xorr
                return
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])
        return result