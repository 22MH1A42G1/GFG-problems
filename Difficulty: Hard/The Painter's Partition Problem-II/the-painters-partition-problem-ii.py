class Solution:
    def isPossible(self,arr,k,val):
        gaps=1
        curr=0
        for item in arr:
            curr+=item
            if curr>val:
                curr=item
                gaps+=1
            if gaps>k:
                return False
        return True

    def minTime (self, arr, k):
        l,h=max(arr),sum(arr)
        while l<=h:
            mid=(l+h)//2
            if self.isPossible(arr,k,mid):
                h=mid-1
            else:
                l=mid+1
        return h+1
