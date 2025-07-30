class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        preSum={0:1}
        currSum=0
        ans=0
        for item in arr:
            currSum+=item
            ans+=preSum.get(currSum-k,0)
            preSum[currSum]=preSum.get(currSum,0)+1
        return ans