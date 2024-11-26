#User function Template for python3
import sys
#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    p, ms, s = 0, -sys.maxsize - 1, 0
    for i in arr:
        s += i
        p += i
        ms = max(ms, s)
        s = max(s, 0)
    cs = 0
    for i in arr:
        cs += i
        cs = min(0, cs)
        ms = max(ms, p - cs)
    return ms
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends