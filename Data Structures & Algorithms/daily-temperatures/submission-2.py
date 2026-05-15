class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        for i in range(len(temperatures)):
            j=i+1
            while (j!=len(temperatures) and temperatures[j]<=temperatures[i]):
                j+=1
            if j!=len(temperatures) and temperatures[j]>temperatures[i]:
                st.append(j-i)
            else:
                st.append(0)
        return st