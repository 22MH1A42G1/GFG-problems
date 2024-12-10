#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals=sorted(intervals,key=lambda x:x[1])
        c=0
        cur=intervals[0]
        for i in intervals[1:]:
            if cur[1]>i[0]:
                c+=1
            else:
                cur=i
        return c

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends