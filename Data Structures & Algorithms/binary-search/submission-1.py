class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start,stop):
            if start>stop:
                return -1
            mid=(start+stop)//2
            if target>nums[mid]:
                return binary(mid+1,stop)
            elif target<nums[mid]:
                return binary(start,mid-1)
            else:
                return mid
        return binary(0,len(nums)-1)

