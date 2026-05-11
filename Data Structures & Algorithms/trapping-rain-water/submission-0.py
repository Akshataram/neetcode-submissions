class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        res=0
        leftmax=height[i]
        rightmax=height[j]
        while(i<j):
            if(leftmax<=rightmax):
                i+=1
                leftmax=max(leftmax,height[i])
                res+=leftmax-height[i]
            else:
                j-=1
                rightmax=max(rightmax,height[j])
                res+=rightmax-height[j]
        return res
