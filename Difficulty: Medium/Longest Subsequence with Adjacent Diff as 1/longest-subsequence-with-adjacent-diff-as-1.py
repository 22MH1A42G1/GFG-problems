class Solution:
    def longestSubseq(self, arr):
        # code here
        from collections import defaultdict
        dp = defaultdict(int)
        res = 0
        for i in arr:
            dp[i] = max(dp[i-1]+1, dp[i+1]+1, 1)
            res = max(res, dp[i])
        return res