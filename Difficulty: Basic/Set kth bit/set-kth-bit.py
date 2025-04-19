#User function Template for python3
class Solution:
	def setKthBit(self, n, k):
		# code here
        return n|(1<<k)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, K = input().split()
        N = int(N)
        K = int(K)
        ob = Solution()
        ans = ob.setKthBit(N, K)
        print(ans)

# } Driver Code Ends