class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=defaultdict(list)
        for i in strs:
            h="".join(sorted(i))
            s[h].append(i)
        return list(s.values())