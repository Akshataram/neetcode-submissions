class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D=deque()
        R=deque()
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r=R.popleft()
            d=D.popleft()
            if r<d:
                R.append(n+r)
            else:
                D.append(n+d)
        if R:
            return "Radiant"
        else:
            return 'Dire'
