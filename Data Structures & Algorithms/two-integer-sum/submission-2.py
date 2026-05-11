class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=defaultdict(int)
        for i,val in enumerate(nums):
            s[val]=i
        for i in range(len(nums)):
            value=target-nums[i]
            if value in s and i!=s[value]:
                return [i,s[value]]

        