class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=i+1
        while i<len(nums)-1:
            if nums[i]!=nums[j] and j+1-i>k:
                i+=1
                j=i+1
            elif nums[i]!=nums[j] and j+1-i<=k:
                j+=1
            elif nums[i]==nums[j] and j-i<=k:
                return True
            else:
                return False
            if j==len(nums):
                i=i+1
                j=i+1
        return False

