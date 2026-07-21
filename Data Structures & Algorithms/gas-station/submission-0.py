class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left=[0]*len(cost)
        tank=0
        start=0
        for i in range(len(cost)):
            left[i]=gas[i]-cost[i]
        if sum(left) < 0:
            return -1
        for i in range(len(cost)):
            if tank+left[i]<0:
                start=i+1
                tank=0
                continue
            tank+=left[i]
        return start