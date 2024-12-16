#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        pass
        c = a+b
        # d = c[0]
        # e = 0
        # for i in range(1,len(c)):
        #     if c[i] > d:
        #         d=c[i]
        #         e=i
        # return i
        c.sort()
        return c[k-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends