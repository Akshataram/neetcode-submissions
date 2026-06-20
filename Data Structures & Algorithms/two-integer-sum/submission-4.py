class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,val in enumerate(nums):
            d[val]=i
        for i in range(len(nums)):
            a=target-nums[i]
            if a in d and i!=d[a]:
                return [i,d[a]]