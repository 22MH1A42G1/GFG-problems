class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        d={0:-1}
        m=s=0
        for i in range(len(a1)):
            s+=a1[i]-a2[i]
            if s in d:
                m=max(m,i-d[s])
            else:
                d[s]=i
        return m