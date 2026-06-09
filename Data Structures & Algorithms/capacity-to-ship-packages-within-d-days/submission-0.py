class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def binarysearch(start,stop):
            if start>stop:
                return start
            c=0
            d=1
            k=(start+stop)//2
            for w in weights:
                c+=w
                if c>k:
                    c=w
                    d+=1
            if d<=days:
                return binarysearch(start,k-1)
            elif d>days:
                return binarysearch(k+1,stop)
        return binarysearch(max(weights),sum(weights))