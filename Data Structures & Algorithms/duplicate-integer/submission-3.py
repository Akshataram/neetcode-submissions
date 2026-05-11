class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for i,val in enumerate(nums):
            d[val]+=1
            if d[val]>1:
                return True
        return False
        
