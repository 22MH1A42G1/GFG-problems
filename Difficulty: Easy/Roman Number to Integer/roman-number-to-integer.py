class Solution:
    def romanToDecimal(self, s): 
        # code here
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        sum=0
        while i<len(s):
            if i+1<len(s) and dict[s[i]]<dict[s[i+1]]:
                sub=dict[s[i+1]]-dict[s[i]]
                sum=sum+sub
                i=i+2
            else:
                sum=sum+dict[s[i]]
                i=i+1
        
        return sum   