class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        curmin=nums[0]
        totmin=nums[0]
        curmax=nums[0]
        totmax=nums[0]
        for i in nums[1:]:
            curmax=max(curmax+i,i)
            totmax=max(curmax,totmax)
            curmin=min(curmin+i,i)
            totmin=min(curmin,totmin)
        if totmin == total:
            return totmax
        return max(totmax, total - totmin)