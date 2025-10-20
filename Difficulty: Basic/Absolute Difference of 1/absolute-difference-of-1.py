#User function Template for python3



class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        # code here
        l=[]
        for i in arr:
            s = str(i)
            if k>i and i>9 and all(abs(int(s[j])-int(s[j+1]))==1 for j in range(len(s)-1)):
                l.append(i)
        return l