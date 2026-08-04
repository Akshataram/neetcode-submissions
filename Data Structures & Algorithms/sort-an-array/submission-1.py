class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=mergesort(nums[:mid])
            right=mergesort(nums[mid:])
            return merge(left,right)
        def merge(a,b):
            i=0
            j=0
            res=[]
            while i<len(a) and j<len(b):
                if a[i]<=b[j]:
                    res.append(a[i])
                    i+=1
                else:
                    res.append(b[j])
                    j+=1
            res.extend(a[i:])
            res.extend(b[j:])
            return res
        return mergesort(nums)
