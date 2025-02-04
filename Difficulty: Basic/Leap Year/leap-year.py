#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        if (n%4 == 0 and n%100!=0) or (n%4 == 0 and n%400==0):
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        if ob.checkYear(N):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends