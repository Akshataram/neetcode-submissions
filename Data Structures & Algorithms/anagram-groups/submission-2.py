class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            t=sorted(s)
            t="".join(t)
            d[t].append(s)
        a=list(d.values())
        return a