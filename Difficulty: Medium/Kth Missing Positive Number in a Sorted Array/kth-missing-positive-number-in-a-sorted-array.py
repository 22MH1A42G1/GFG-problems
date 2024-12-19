#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        s=1
        for i in arr:
            if i-s and k<=(i-s):
                return s+k-1
            else:
                k-=(i-s)
            s=i+1
        if k:
            k-=1
        return s+k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends