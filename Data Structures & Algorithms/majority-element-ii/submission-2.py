class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=[]
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for i in nums:
            if d[i] and d[i]>(len(nums)/3):
                a.append(i)
                del d[i]
        return a

