class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        mp=dict()
        cnt,l=0,0
        for i in range(len(arr)):
            if arr[i] not in mp:
                mp[arr[i]]=1
            else:
                mp[arr[i]]+=1
            while len(mp)>k:
                mp[arr[l]]-=1
                if mp[arr[l]]==0:
                    del mp[arr[l]]
                l+=1
            cnt+=i-l+1
        return cnt