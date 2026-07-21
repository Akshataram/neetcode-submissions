class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        seti=set()
        start=0
        for i,val in enumerate(s):
            seti.add(val)
            d[val]-=1
            if d[val]==0:
                seti.remove(val)
            if not seti:
                res.append(i-start+1)
                start=i+1
        return res


