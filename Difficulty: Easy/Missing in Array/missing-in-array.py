class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)+1
        sn = n*(n+1)//2
        sa = sum(arr)
        return sn-sa if n>1 else 2

