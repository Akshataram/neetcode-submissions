class Solution:
    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            n=len(s)
            m=str(n)+"@"+s
            string+=m
        return string
        
    def decode(self, s: str) -> List[str]:
        i=0
        strs=[]
        while(i<len(s)):
            j=i
            while(s[j]!="@"):
                j+=1
            a=int(s[i:j])
            strs.append(s[j+1:j+1+a])
            i=j+1+a
        return strs