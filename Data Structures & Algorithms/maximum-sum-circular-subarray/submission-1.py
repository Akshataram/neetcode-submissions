class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        gm=nums[0]
        total=0
        gn=nums[0]
        cm=0
        cn=0
        for i in nums:
            cm=max(cm+i,i)
            gm=max(gm,cm)
            cn=min(cn+i,i)
            gn=min(gn,cn)
            total+=i
        if gm>0:
            return max(gm,total-gn)
        else:
            return gm