class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(index,path):
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                num=candidates[i]
                if num+sum(path[:])>target:
                    continue
                path.append(num)
                if sum(path[:])==target:
                    if path[:] not in res:
                        res.append(path[:])
                else:
                    backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res
