class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=defaultdict(int)
        for i,val in enumerate(nums):
            s[val]+=1
            if s[val]>(len(nums)/2):
                return val