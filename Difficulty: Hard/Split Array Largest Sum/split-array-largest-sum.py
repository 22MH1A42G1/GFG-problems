class Solution:
    def check(self,arr,k,m):
        t,c=0,1
        for i in arr:
            if i>m:
                return False
            t+=i
            if t>m:
                t=i
                c+=1
        return k>=c
    def splitArray(self, arr, k):
        # code here
        l,h=max(arr),sum(arr)
        while l<=h:
            m=(l+h)//2
            if self.check(arr,k,m):
                h=m-1
            else:
                l=m+1
        return l