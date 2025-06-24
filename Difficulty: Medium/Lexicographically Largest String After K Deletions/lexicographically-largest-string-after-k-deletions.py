class Solution:
    def maxSubseq(self, s, k):
        #code here
        n = len(s)
        res = ""
        to_remove = k  
        for i in range(n):
            while res and to_remove > 0 and res[-1] < s[i]:
                res = res[:-1]
                to_remove -= 1
            res += s[i]
        return res[:n-k]

        
