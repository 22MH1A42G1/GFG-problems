class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n, m = len(s1), len(s2)
        np = [[-1] * 26 for _ in range(n + 2)]
        for i in range(26): np[n][i]=-1
        for i in range(n-1,-1,-1):
            for j in range(26): np[i][j]=np[i+1][j]
            np[i][ord(s1[i])-ord('a')]=i
        ans, ml = "", float("inf")
        for i in range(n):
            if s1[i]!=s2[0]: continue
            idx=i
            ok=True
            for j in range(m):
                if idx==-1:
                    ok=False
                    break
                idx=np[idx][ord(s2[j])-ord("a")]
                if idx==-1:
                    ok=False
                    break
                idx+=1
            if ok:
                ei=idx-1
                l=ei-i+1
                if l<ml:
                    ml=l
                    ans=s1[i:i+l]
        return ans
        