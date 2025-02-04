#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        a,b,c,d=0,0,0,0
        for i in s:
            if i.isupper():
                a+=1
            elif i.islower():
                b+=1
            elif i.isdigit():
                c+=1
            else:
                d+=1
        return a,b,c,d


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends