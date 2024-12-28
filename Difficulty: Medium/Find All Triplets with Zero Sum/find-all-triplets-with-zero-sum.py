#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        n=len(arr)
        ans=[]
        for i in range(n-1):
            dic={arr[i+1]:[i+1]}
            for j in range(i+2,n):
                if 0-arr[i]-arr[j] in dic:
                    for x in dic[0-arr[i]-arr[j]]:
                        ans.append([i,x,j])
                if arr[j] not in dic: dic[arr[j]]=[j]
                else: dic[arr[j]].append(j)
        return ans

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends