#User function Template for python3

class Solution:
    def nQueen(self, n):
        bd=[None]*n
        rw=set()
        up=set()
        dn=set()
        ret=[]
        def bt(x=0):
            nonlocal n,bd,rw,up,dn,ret
            if x==n:
                return True
            for y in range(n):
                if y in rw or y+x in up or y-x in dn:
                    continue
                bd[x]=y
                rw.add(y)
                up.add(y+x)
                dn.add(y-x)
                if bt(x+1):
                    ret.append([x+1 for x in bd])
                bd[x]=None
                rw.discard(y)
                up.discard(y+x)
                dn.discard(y-x)
        bt()
        return ret

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends