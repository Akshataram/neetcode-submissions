class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            n=len(i)
            s+=str(n)+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        r=[]
        while(i<len(s)):
            b=""
            while(s[i]!="#"):
                b+=s[i]
                i+=1
            b=int(b)
            r.append(s[i+1:b+i+1])
            i=b+i+1
        return r