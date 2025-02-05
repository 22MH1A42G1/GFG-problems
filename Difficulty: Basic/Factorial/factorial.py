#User function Template for python3


class Solution:
    def factorial (self, n):
        # code here
        if n==0 or  n==1: return 1
        fact = n*self.factorial(n-1)
        return fact
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

        print("~")

# } Driver Code Ends