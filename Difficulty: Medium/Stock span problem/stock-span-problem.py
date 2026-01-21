class Solution:
    def calculateSpan(self, arr):
        # code here
        
        span = []
        
        stack = [(float("inf"),-1)]
        
        for i in range(len(arr)):
            
            while(stack and stack[-1][0]<=arr[i]):
                stack.pop()
            
            span.append(i-stack[-1][1])
            
            stack.append((arr[i],i))
        
        return span