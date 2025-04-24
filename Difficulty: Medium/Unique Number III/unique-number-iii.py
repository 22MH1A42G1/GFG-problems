#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        from collections import Counter
        c = Counter(arr)
        for i,j in c.items():
            if j==1:
                return i
        return 1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends