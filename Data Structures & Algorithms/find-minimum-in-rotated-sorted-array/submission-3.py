class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(start,stop):
            if start-stop==0:
                return nums[start]
            mid=(start+stop)//2
            if nums[mid]>nums[stop]:
                return binary(mid+1,stop)
            else:
                return binary(start,mid)
        return binary(0,len(nums)-1)