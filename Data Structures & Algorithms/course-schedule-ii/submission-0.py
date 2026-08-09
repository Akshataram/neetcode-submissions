class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            premap[i].append(j)
        visited=list()
        cycle=set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for i in premap[crs]:
                if not dfs(i):
                    return False
            cycle.remove(crs)
            visited.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return visited