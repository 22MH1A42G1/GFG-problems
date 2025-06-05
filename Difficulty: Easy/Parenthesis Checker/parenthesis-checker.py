
class Solution:
    def isBalanced(self, s):
        # code here
        p = {")":"(", "}":"{", "]":"["}
        st = []
        for i in s:
            if i in p.values():
                st.append(i)
            elif i in p:
                if not st or st.pop()!=p[i]:
                    return False
        return not st