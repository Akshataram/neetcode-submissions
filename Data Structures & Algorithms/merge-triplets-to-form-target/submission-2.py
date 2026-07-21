class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        d,e,f=0,0,0
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]:
                d=1
            if b==target[1]:
                e=1
            if c==target[2]:
                f=1
        if d==1 and e==1 and f==1:
            return True
        else:
            return False
