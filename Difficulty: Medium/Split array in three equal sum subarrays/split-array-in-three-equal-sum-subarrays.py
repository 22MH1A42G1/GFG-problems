#User function Template for python3
class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        #cod here
        n=len(arr)
        total_sum=sum(arr)
        equal_sum=total_sum//3
        pre=0
        se=0
        if total_sum % 3==0:
            for i in range(n):
                pre +=arr[i]
                if pre == equal_sum :
                    se+=1
                    pre=0
                    if se==2:
                        return True
            return [-1,-1]            
        else:
            return [-1,-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")
        print("~")

# } Driver Code Ends