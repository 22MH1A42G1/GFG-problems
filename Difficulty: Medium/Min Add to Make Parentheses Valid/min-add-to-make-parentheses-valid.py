class Solution:
    def minParentheses(self, s):
        # code here
        st = []
        count = 0
        for c in s:
            if c==')':
                if not st:
                    count += 1
                else:
                    st.pop()
            elif c=='(':
                st.append(c)
        count += len(st)
        return count
        