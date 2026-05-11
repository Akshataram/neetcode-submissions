class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=defaultdict(int)
        for i,val in enumerate(nums):
            s[val]+=1
            if s[val]>1:
                return True
        return False