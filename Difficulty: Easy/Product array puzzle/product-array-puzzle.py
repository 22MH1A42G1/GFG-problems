#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here  arr[] = [10, 3, 5, 6, 2]
        n=len(arr) #5
        lp=[1]*(n)
        rp=[1]*(n)
        p=1
        for i in range(len(arr)):
            p*=arr[i]
            lp[i]=p #lp[] = [10, 30, 150, 900, 1800]
        np=1
        for i in range(n-1,-1,-1):
            np*=arr[i]
            rp[i]=np #rp[] = [1800, 180, 60, 12, 2]
        ans=[1]*n
        for i in range(1,n-1):
            ans[i]=lp[i-1]*rp[i+1] 
            """
            ans[1] = lp[0]*rp[2] = 10*60 = 600
            ans[2] = lp[1]*rp[3] = 30*12 = 360
            ans[3] = lp[2]*rp[4] = 150*2 = 300
            """
        ans[0]=rp[1] # ans[0] = 180
        ans[n-1]=lp[n-2]# ans[4] = 900
        return ans # [180, 600, 360, 300, 900]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends