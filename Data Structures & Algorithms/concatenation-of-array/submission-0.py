class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=list()
        n=len(nums)
        for i in range(2*len(nums)):
            if i>=n:
                ans.append(nums[i-n])
            else:
                ans.append(nums[i])
        return ans
