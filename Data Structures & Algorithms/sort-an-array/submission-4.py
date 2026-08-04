class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums,low,high):
            if low<high:
                pivot=partition(nums,low,high)
                quicksort(nums,low,pivot-1)
                quicksort(nums,pivot+1,high)
        def partition(nums,low,high):
            mid = (low + high) // 2
            nums[low], nums[mid] = nums[mid], nums[low]
            a=nums[low]
            i=low+1
            j=high
            while True:
                while i<=high and nums[i]<=a:
                    i+=1
                while j>low and nums[j]>a:
                    j-=1
                if i<j:
                    nums[i],nums[j]=nums[j],nums[i]
                else:
                    break
            nums[low],nums[j]=nums[j],nums[low]
            return j
        quicksort(nums,0,len(nums)-1)
        return nums
        
            


            