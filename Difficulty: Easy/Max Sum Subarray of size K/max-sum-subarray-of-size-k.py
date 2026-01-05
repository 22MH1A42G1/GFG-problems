class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        maxi=sum(arr[:k])
        ans=maxi
        l=0
        for i in arr[k:]:
           if l<len(arr):
                maxi+=i
                maxi-=arr[l]
                ans=max(ans,maxi)
                l+=1
                
        return ans