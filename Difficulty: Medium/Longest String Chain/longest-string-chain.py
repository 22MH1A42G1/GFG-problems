#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        c = {} 
        s = sorted(words, key=len)
        for w in s:
            c[w] = 1 
            for i in range(len(w)):
                p = w[:i] + w[i+1:]
                if p in c:
                    c[w] = max(c[w], c[p] + 1)
        return max(c.values())


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends