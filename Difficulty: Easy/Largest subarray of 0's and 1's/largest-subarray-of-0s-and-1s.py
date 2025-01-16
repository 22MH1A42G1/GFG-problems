class Solution:
    def maxLen(self, arr):
        # code here
        c,m,p=0,0,{0:-1}
        for i,a in enumerate(arr):
            c+=1 if a else -1
            if c in p:
                l = i-p[c]
                if l > m:
                    m=l
            else:
                p[c]=i
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends