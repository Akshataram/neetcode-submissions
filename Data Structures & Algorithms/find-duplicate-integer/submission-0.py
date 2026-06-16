from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            if d[num]:
                return num
            d[num] += 1