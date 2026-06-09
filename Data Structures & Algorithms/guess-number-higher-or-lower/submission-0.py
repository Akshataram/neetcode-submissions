# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary(start,stop):
            mid=(start+stop)//2
            if guess(mid)==0:
                return mid
            elif(guess(mid)==-1):
                return binary(start,mid-1)
            else:
                return binary(mid+1,stop)
        return binary(1,n)