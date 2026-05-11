class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=defaultdict(int)
        res=0
        for num in nums:
            if not s[num]:
                s[num]=s[num-1]+s[num+1] +1
                s[num-s[num-1]]=s[num]
                s[num+s[num+1]]=s[num]
                res=max(res,s[num])
        return res