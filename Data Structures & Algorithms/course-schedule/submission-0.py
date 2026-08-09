class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            dict[i].append(j)
        visitedset=set()
        def dfs(crs):
            if crs in visitedset:
                return False
            if dict[crs]==[]:
                return True
            visitedset.add(crs)
            for i in dict[crs]:
                if not dfs(i):
                    return False
            visitedset.remove(crs)
            dict[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
