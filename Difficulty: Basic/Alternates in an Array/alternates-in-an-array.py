#User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr):
    # your code here
    n = len(arr)
    for j in range(0,n,2):
        print(arr[j], end =" ")





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        printAl(arr)
        print()

# } Driver Code Ends