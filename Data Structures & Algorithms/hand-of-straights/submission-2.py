class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        s=defaultdict(int)
        for i in hand:
            s[i]+=1
        hand.sort()
        for i in hand:
            if s[i]==0:
                continue
            for j in range(i,i+groupSize):
                if s[j]==0:
                    return False
                s[j]-=1
        return True