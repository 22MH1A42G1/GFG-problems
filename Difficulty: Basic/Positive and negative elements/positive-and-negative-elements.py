#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3



class Solution:
    def arranged(self,arr):
        #Code here
        p=[]
        n=[]
        for i in arr:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        new = []
        l = len(arr)
        for i in range(l//2):
            new.append(p[i])
            new.append(n[i])
        return new
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.arranged(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends