#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
        result=""
        m,n,carry=len(s1)-1,len(s2)-1,0
        while m>=0 or n>=0 or carry!=0:
            a=int(s1[m]) if m>=0 else 0
            b=int(s2[n]) if n>=0 else 0
            temp=(a+b+carry)
            result=str(temp%2)+result
            carry=temp//2
            m-=1
            n-=1
        return result.lstrip("0")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends