class Solution:
	def minJumps(self, arr):
	    # code here
	    a,b,c=0,-1,0
	    while a<len(arr)-1:
	        mx = max([b+1+i+e for i,e in enumerate(arr[b+1:a+1])])
	        if mx>a:
	            a,b,c=mx,a,c+1
	        else:
	            return -1
	    return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends