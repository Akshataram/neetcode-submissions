class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=stones
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while len(nums)>=2:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            if a==b:
                pass
            else:
                c=b-a
                heapq.heappush(nums,-c)
        if len(nums)==1:
            return -nums[0]
        else:
            return 0

            
