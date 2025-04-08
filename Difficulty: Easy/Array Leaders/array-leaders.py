class Solution:
    def leaders(self, arr):
        # code here
        j=[]
        m=arr[-1]
        j.append(m)
        for i in range(1,len(arr)+1):
            if m<=arr[-i]:
                m=arr[-i]
                j.append(m)
                #print(m,arr[-i])
        return j[::-1][:-1]

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends