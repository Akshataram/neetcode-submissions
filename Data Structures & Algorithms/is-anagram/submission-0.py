class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in s:
            n[i]+=1
        for i in t:
            n[i]-=1
        for i in s:
            if n[i]!=0:
                return False
        return True