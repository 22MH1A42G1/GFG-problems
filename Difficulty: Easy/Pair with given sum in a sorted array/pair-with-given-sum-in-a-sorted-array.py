#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        n=len(arr)
        i,j=0,n-1
        ans=0
        while i<=j:
            s = arr[i]+arr[j]
            if s == target:
                c1,v1 = 0, arr[i]
                c2,v2 = 0, arr[j]
                while i<=j and arr[i]==v1:
                    c1+=1
                    i+=1
                while i<=j and arr[j]==v2:
                    c2+=1
                    j-=1
                if v1==v2:
                    ans+=c1*(c1-1)//2
                else:
                    ans+=c1*c2
            elif s > target:
                j-=1
            else:
                i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends