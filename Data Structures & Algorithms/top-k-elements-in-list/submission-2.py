class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        s=[]
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        a=list(d.items())
        for i,j in a:
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        for i,val in heap:
            s.append(val)
        return s