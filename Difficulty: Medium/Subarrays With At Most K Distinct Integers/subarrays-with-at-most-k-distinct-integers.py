from collections import defaultdict
class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        l,r=0,0
        n=len(arr)
        cnt=0
        mp=defaultdict(int)
        while(r<n):
            mp[arr[r]]+=1         
            while(len(mp)>k):
                mp[arr[l]]-=1
                if(mp[arr[l]]==0):
                    del mp[arr[l]]
                l+=1
            cnt+=(r-l+1)
            r+=1
        return cnt

