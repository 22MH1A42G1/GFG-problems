#User function Template for python3

class Solution:
    def greatestOfThree(self,A,B,C):
        #code here
        return max(A,B,C)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
        print("~")
# } Driver Code Ends