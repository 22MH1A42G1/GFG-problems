#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        c,i,j=0,0,len(arr)-1
        while i<j:
            if arr[i]+arr[j]<target:
                c+=j-i
                i+=1
            else:
                j-=1
        return c
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends