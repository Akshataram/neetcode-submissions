class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,val in enumerate(nums):
            d[val]=i
        for i in range(len(nums)):
            s=target-nums[i]
            if (s in d and i!=d[s]):
                return [i,d[s]]