class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i,val in enumerate(nums):
            if val>0:
                break
            if i>0 and val==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            targ=-val
            while(l<r):
                if nums[l]+nums[r]==targ:
                    a.append([val,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif(nums[l]+nums[r]<targ):
                    l+=1
                else:
                    r-=1
        return a
