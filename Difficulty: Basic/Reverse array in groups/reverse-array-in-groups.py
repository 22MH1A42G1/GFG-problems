#User function template for Python

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        n =len(arr)
        for i in range(0,n,k):
            arr[i:i+k]=reversed(arr[i:i+k])

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    line_index = 1
    for _ in range(t):
        k = int(data[line_index])
        line_index += 1
        arr = list(map(int, data[line_index].split()))
        line_index += 1
        ob = Solution()
        ob.reverseInGroups(arr, k)
        print(" ".join(map(str, arr)))
        print("~")

# } Driver Code Ends