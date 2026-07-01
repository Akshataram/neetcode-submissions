class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        window=set()
        j=0
        maxlen=0
        for i in range(len(nums)):
            while nums[i] in window:
                n=len(window)
                window.remove(nums[j])
                j+=1
            window.add(nums[i])
            maxlen=max(maxlen,i-j+1)
        return maxlen

