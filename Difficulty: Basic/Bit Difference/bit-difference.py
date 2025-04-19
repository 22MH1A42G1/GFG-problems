#User function Template for python3

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        ##Your code here
        c,t=0,a^b
        while t>0:
            c+=t&1
            t>>=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        ob = Solution()
        print(ob.countBitsFlip(a, b))
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends