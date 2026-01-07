class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        res=[]
        d={}
        for i in range(k):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        l=0
        res.append(len(d))
        for r in range(k,n):
            if arr[r] in d:
                d[arr[r]]+=1
            else:
                d[arr[r]]=1
            d[arr[l]]-=1
            if d[arr[l]]==0:
                del d[arr[l]]
            l+=1
            res.append(len(d))
        return res