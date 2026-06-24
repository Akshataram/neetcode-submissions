class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]*len(nums)
        res=[1]*len(nums)
        suf=[1]*len(nums)
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suf[j]=suf[j+1]*nums[j+1]
        for m in range(len(nums)):
            res[m]=pref[m]*suf[m]
        return res
