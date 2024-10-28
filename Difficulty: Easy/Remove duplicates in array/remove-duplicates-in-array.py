#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

import numpy as np
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        a = []
        for i in arr:
            if i not in a:
                a.append(i)
        return a

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends