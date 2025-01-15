# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        x = {0:0}
        l = 0
        csum = 0
        for i in range(len(arr)):
            csum+=arr[i]
            if csum-k in x:
                l = max(l,i-x[csum-k]+1)
            if csum not in x:
                x[csum]=i+1
        return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends