class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        return max(max(left,default=0),n-min(right,default=n))