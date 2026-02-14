class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        i =j=k=0
        n = len(a)
        ans = []
        minDiff = float('inf')
        while i<n and j<n and k<n:
            aVal , bVal , cVal = a[i], b[j], c[k]
            maxi = max(aVal , bVal , cVal)
            mini = min(aVal , bVal , cVal)
            if maxi-mini<minDiff:
                minDiff = maxi-mini
                ans = [aVal , bVal , cVal]
            if mini == aVal:
                i+=1
            elif mini == bVal:
                j+=1
            else:
                k+=1
        return sorted(ans , reverse=True)
