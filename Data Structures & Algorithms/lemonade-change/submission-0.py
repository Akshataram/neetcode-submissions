class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ch=0
        f=0
        t=0
        for b in bills:
            if b==5:
                f+=1
            elif b==10:
                t+=1
                f-=1
            elif t>0:
                t-=1
                f-=1
            else:
                f-=3
            if f<0:
                return False
        return True

            