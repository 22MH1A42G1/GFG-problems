class Solution:
    def sumSubMins(self, arr):
        # Code here
        n=len(arr)
        prev_less,next_less=[None]*n,[None]*n
        stack_p,stack_n=[],[]
        for i in range(n):
            while stack_p and arr[stack_p[-1]]>arr[i]:
                stack_p.pop()
            prev_less[i]=stack_p[-1] if stack_p else -1
            stack_p.append(i)
            while stack_n and arr[stack_n[-1]]>=arr[n-1-i]:
                stack_n.pop()
            next_less[n-1-i]=stack_n[-1] if stack_n else n
            stack_n.append(n-1-i)
        ans=0
        for i in range(n):
            left=i-prev_less[i]
            right=next_less[i]-i
            ans+=arr[i]*left*right
        return ans