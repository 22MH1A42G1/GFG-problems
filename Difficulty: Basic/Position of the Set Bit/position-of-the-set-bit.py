class Solution:
    def findPosition(self, n):
        # code here 
        if n==0:return -1
        if n&(n-1)==0:
            return n.bit_length()
        return -1