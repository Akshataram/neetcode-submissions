class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        target=0
        nums.sort()
        for i,val in enumerate(nums):
            if(val>0):
                break
            if(i>0 and val==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                target=val+nums[j]+nums[k]
                if(target==0):
                    res.append([val,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif(target<0):
                    j+=1
                else:
                    k-=1
        return res

