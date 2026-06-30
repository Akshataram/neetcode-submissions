class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        n=set()
        for i in nums:
            if i not in n:
                n.add(i)
                nums[k]=i
                k+=1
            else:
                continue
        return k