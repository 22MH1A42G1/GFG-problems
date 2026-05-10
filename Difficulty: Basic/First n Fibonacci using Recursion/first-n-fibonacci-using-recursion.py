#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        l=[-1]*n
        for i in range(n):
            if i<=1:
                l[i]=i
            else:
                l[i]=l[i-1]+l[i-2]
        return l