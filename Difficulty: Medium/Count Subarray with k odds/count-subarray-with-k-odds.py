class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        def atmost(arr,k):
            n=len(arr)
            o=0
            ans=0
            s=0
            for i in range(n):
                if arr[i]%2!=0:
                    o+=1
                while o>k:
                    if arr[s]%2!=0:
                        o-=1
                    s+=1
                ans+=i-s+1
            return ans
        n=len(arr)
        x=atmost(arr,k)
        y=atmost(arr,k-1)
        return x-y