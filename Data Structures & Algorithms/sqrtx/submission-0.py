class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(start,stop):
            if start>stop:
                return stop
            mid=(start+stop)//2
            if (mid*mid)>x:
                return binary(start,mid-1)
            elif((mid*mid)<x):
                return binary(mid+1,stop)
            else:
                return mid
        return binary(0,x)