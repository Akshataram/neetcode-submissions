class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binarysearch(start,stop):
            if start>stop:
                return start
            k=(start+stop)//2
            a=0
            for i in piles:
                a+=math.ceil((i/k))
            if a>h:
                return binarysearch(k+1,stop)
            if a<=h:
                return binarysearch(start,k-1)

        return binarysearch(1,max(piles))    