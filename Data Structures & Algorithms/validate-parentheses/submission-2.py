class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in {"(","[","{"}:
                st.append(i)
            if i==")":
                if st and st[-1]=="(":
                    st.pop()
                else:
                    return False
            if i=="]":
                if st and st[-1]=="[":
                    st.pop()
                else:
                    return False
            if i=="}":
                if st and st[-1]=="{":
                    st.pop()
                else:
                    return False
        if len(st)==0:
            return True
        else:
            return False
    