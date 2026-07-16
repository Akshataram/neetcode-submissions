class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cm=nums[0]
        m=nums[0]
        for i in nums[1:]:
            cm=max(cm+i,i)
            m=max(cm,m)
        return m