class Solution:
	def kLargest(self, arr, k):
		# Your code here
		arr.sort()
		l = []
		for i in range(1,k+1):
		    l.append(arr[len(arr)-i])
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends