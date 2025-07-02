class Solution:
    def totalElements(self, arr):
        # Code here
        i=0
        j=0
        ans=0
        dict={}
        
        for k in arr:
            dict[k]=dict.get(k,0)+1
            while len(dict)>2:
                dict[arr[i]]-=1
                if dict[arr[i]]==0:
                    dict.pop(arr[i])
                i+=1
            
            if len(dict)<=2:
                ans=max(ans,j-i+1)
            j+=1
        return ans