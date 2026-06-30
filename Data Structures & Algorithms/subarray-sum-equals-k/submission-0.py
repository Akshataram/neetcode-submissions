class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        prefix=0
        count=0
        for n in nums:
            prefix+=n
            if d[prefix-k]:
                count+=d[prefix-k]
            d[prefix]+=1
        return count
