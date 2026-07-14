from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s=defaultdict(list)
        heap,e=[],[]
        for i,n in points:
            a=sqrt(i**2 +n**2)
            s[a].append([i,n])
            heapq.heappush(heap,a)
        while k>0:
            d=heapq.heappop(heap)
            b,c=s[d].pop()
            e.append([b,c])
            k-=1
        return e


