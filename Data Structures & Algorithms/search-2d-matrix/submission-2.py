class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(start,stop,mid):
            midi=(start+stop)//2
            if start>stop:
                return False
            a=matrix[mid][midi]
            if a>target:
                return binary(start,midi-1,mid)
            elif a<target:
                return binary(midi+1,stop,mid)
            else:
                return True
        def binarysearch(start,stop):
            mid=(start+stop)//2
            if start>stop:
                return False
            if matrix[mid][0]>target:
                return binarysearch(start,mid-1)
            elif matrix[mid][0]<target and matrix[mid][-1]<target:
                return binarysearch(mid+1,stop)
            else:
                return binary(0,len(matrix[mid])-1,mid)
        return binarysearch(0,len(matrix)-1)
