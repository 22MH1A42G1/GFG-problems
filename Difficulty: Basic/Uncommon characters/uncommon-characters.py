#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        l1,l2 = list(s1), list(s2)
        l3 = []
        for i in s1:
            for j in s2:
                if i not in s2 and i not in l3:
                    l3.append(i)
                if j not in s1 and j not in l3:
                    l3.append(j)
        return "".join(sorted(l3))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.uncommonChars(A, B))

        print("~")
# } Driver Code Ends