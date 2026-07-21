class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        s=defaultdict(int)
        count=0
        for i in hand:
            s[i]+=1
        if len(hand) % groupSize != 0:
            return False
        while s:
            a=min(s)
            while(count<groupSize):
                if a in s:
                    s[a]-=1
                    if s[a]==0:
                        del s[a]
                    count+=1
                else:
                    return False
                a=a+1
            count=0
        return True

                
