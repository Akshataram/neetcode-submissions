class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=defaultdict(int)
        for ind,val in enumerate(nums):
            if(a[val]!=0):
                return True
            a[val]+=1
        return False


