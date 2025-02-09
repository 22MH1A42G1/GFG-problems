#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        dp=[-1]*n
        for i in range(n):
            if i<=1:
               dp[i]=i
            else:
                dp[i]=dp[i-1]+dp[i-2]
        return dp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().fibonacciNumbers(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends