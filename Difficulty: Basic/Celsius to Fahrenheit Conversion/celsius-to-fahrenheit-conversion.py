#User function Template for python3


class Solution:
    def celciusToFahrenheit (self, C):
        # code here
        return C*(9/5)+32


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print('%.2f'%ob.celciusToFahrenheit(N))
        print("~")
# } Driver Code Ends