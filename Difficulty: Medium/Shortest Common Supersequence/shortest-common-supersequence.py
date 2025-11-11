class Solution:
    def minSuperSeq(self, s1, s2):
        # code here
        
        n,m=len(s1),len(s2)
        dp = [[0]*(m+1) for i in range(n+1) ]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1],dp[i-1][j])
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return n+m-dp[-1][-1]