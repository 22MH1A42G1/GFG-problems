class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        st=[]
        for i in s[::-1]:
            st.append(i)
        return "".join(st)