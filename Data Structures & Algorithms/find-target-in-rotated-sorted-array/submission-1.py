class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(start,stop):
            if start>stop:
                return -1
            mid=(start+stop)//2
            if nums[mid]==target:
                return mid
            if nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    return binary(start,mid)
                else:
                    return binary(mid+1,stop)
            else:
                if nums[mid]<target<=nums[stop]:
                    return binary(mid+1,stop)
                else:
                    return binary(start,mid)
        return binary(0,len(nums)-1)