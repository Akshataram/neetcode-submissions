class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=0
        i=0
        j=0
        window=set()
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i+=1
            window.add(s[j])
            cnt=max(cnt,len(window))
        return cnt

