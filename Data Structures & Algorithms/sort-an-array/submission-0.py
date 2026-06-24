class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a,b):
            i=0
            j=0
            merged=[]
            while i<len(a) and j<len(b):
                if a[i]>=b[j]:
                    merged.append(a[i])
                    i+=1
                else:
                    merged.append(b[j])
                    j+=1
            while(i<len(a)):
                merged.append(a[i])
                i+=1
            while(j<len(b)):
                merged.append(b[j])
                j+=1
            return merged
        def mergesort(a):
            if len(a)<=1:
                return a
            mid=len(a)//2
            return merge(mergesort(a[:mid]),mergesort(a[mid:]))
        return mergesort(nums)[::-1]
