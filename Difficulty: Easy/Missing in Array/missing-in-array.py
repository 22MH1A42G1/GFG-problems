#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)+1
        sn = n*(n+1)//2
        sa = sum(arr)
        return sn-sa if n>1 else 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends