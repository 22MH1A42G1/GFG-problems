from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here arr = [4, 2, 2, 6, 4]; k = 6
        px = defaultdict(int, {0: 1})
        """
        defaultdict(
            <class 'int'>,
            {0: 1}
            )
        """
        cx, c = 0, 0
        for i in arr:
            cx ^= i #0^4=4,4^2=6,6^2=4,4^6=2,2^4=6
            c += px[cx ^ k] 
            """
            c=0,1,1,3,4,4
            px[4^6=2]=0,
            px[6^6=0]=1,
            px[4^6=2]=0,
            px[2^6=4]=2,
            px[6^6=0]=1
            """
            #print(c,px)
            """
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 2,
                6: 1
            })
            """
            px[cx] += 1 #px+={4:1},px+={6:1},px+={4:2},px[2:1]
            """
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 1,
                6: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 1,
                6: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 0,
                4: 2,
                6: 1
            })
            defaultdict(<class 'int'>, {
                0: 1, 
                2: 1,
                4: 2,
                6: 1
            })
            """
            #print(px)
        return c


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends