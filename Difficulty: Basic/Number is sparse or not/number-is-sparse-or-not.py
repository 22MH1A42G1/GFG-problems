#User function Template for python3

class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        s=0
        while n:
            if n&1:
                s+=1
            elif s>0:
                s=s-1
            n=n>>1   
            if s>1:
                return 0
        return 1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends