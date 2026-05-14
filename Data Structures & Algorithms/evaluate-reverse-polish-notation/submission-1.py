class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i=="+":
                a=st.pop()
                b=st.pop()
                c=a+b
                st.append(c)
            elif i=="*":
                a=st.pop()
                b=st.pop()
                c=a*b
                st.append(c)
            elif i=="-":
                a=st.pop()
                b=st.pop()
                c=b-a
                st.append(c)
            elif i=="/":
                a=st.pop()
                b=st.pop()
                if a!=0:
                    c=int(b / a)
                else:
                    return -1
                st.append(c)
            else:
                st.append(int(i))
        if len(st)!=1:
            return -1
        else:
            return st[-1]
            