class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        i=0
        j=i+1
        profit=0
        while j!=len(nums):
            if nums[i]<nums[j]:
                profit=max(profit,nums[j]-nums[i])
                j+=1
            else:
                i=j
                j=i+1
        return profit