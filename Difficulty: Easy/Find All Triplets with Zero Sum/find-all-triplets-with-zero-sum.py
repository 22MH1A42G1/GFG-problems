#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        n = len(arr)
        arr = [(arr[i],i) for i in range(n)]
        arr.sort()
        ans = []
        for i in range(n-2):
            j,k = i+1,n-1
            while j < k:
                if arr[i][0] + arr[j][0] + arr[k][0] == 0:
                    ans.append(list(sorted([arr[i][1],arr[j][1],arr[k][1]])))
                    #The other option of considering the j++ 
                    for u in range(j+1,k):
                        if arr[i][0] + arr[u][0] + arr[k][0] == 0:
                            ans.append(list(sorted([arr[i][1],arr[u][1],arr[k][1]])))
                    k -= 1
                elif arr[i][0] + arr[j][0] + arr[k][0] > 0:
                    k -= 1
                else:
                    j += 1
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