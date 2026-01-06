class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        x=0
        ans=0
        n=len(arr)
        for i in range(k):
            x^=arr[i]
        ans=max(ans,x)
        l=0
        for i in range(k,n):
            x^=arr[l]
            l+=1
            x^=arr[i]
            ans=max(ans,x)
        return ans