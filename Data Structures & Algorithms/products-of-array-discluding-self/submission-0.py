class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        result=[1]*len(nums)
        for i in range(len(nums)-1):
            prefix[i+1]=nums[i]*prefix[i]
        for i in range(len(nums)-1,0,-1):
            suffix[i-1]=nums[i]*suffix[i]
        for i in range(len(nums)):
            result[i]=prefix[i]*suffix[i]
        return result       
        