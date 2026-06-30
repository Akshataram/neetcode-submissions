class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        a=[]
        cand1,cand2=-1,-1
        cnt1,cnt2=0,0
        for n in nums:
            if n==cand1:
                cnt1+=1
            elif n==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1=n
                cnt1=1
            elif cnt2==0:
                cand2=n
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for n in nums:
            if n==cand1:
                cnt1+=1
            if n==cand2:
                cnt2+=1
        if cnt1>len(nums)//3:
            a.append(cand1)
        if cnt2>len(nums)//3:
            a.append(cand2)
        return a