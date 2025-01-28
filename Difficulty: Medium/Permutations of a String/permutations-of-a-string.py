#User function Template for python3
from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        return list(set("".join(i) for i in permutations(s)))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends