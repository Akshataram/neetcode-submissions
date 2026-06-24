class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=[]
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        a=list(d.items())
        a.sort(key=lambda x:-x[1])
        for i in range(k):
            s.append(a[i][0])
        return s
        