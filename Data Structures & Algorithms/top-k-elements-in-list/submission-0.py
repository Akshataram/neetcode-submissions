class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=defaultdict(int)
        for i,val in enumerate(nums):
            s[val]+=1
        result=[]
        h=sorted(s.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(h[i][0])
        return result