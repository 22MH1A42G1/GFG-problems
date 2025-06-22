class Solution:
    def largestSubset(self, arr):
        #code here
        arr.sort()
        n = len(arr)
        idx, l = n-1, 1
        dp = [(1, None) for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            li, k = dp[i]
            for j in range(i+1, n):
                if arr[j]%arr[i] == 0:
                    if dp[j][0] + 1 >= li:
                        li = dp[j][0] + 1
                        k = j
            dp[i] = (li, k)
            if li > l:
                idx = i
                l = li
        
        ans = []
        while idx is not None:
            ans.append(arr[idx])
            idx = dp[idx][1]
        return ans