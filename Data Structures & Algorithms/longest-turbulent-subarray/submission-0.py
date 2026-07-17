class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        curmax=1
        totmax=1
        flipped=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                flipped=0
                curmax=1
                continue
            if nums[i]<nums[i+1]:
                flip=1
            else:
                flip=-1
            if flip==-flipped:
                curmax+=1
            else:
                curmax=2
            totmax=max(curmax,totmax)
            flipped =flip
        return totmax