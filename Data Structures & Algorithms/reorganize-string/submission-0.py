class Solution:
    def reorganizeString(self, s: str) -> str:
        dic=defaultdict(int)
        res=[]
        prev=None
        for i in s:
            dic[i]+=1
        a=list(dic.items())
        a=[[-y,x] for x,y in a]
        heapq.heapify(a)
        while prev or a:
            if not a:
                return ""
            cnt,st=heapq.heappop(a)
            cnt+=1
            res.append(st)
            if prev:
                heapq.heappush(a, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, st]
        return "".join(res)

                



