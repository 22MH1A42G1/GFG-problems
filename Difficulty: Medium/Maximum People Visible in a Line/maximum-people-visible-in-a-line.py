class Solution:
    def maxPeople(self, arr):
        # code here
        n=len(arr)
        prev_larg=[-1]*n
        next_larg=[n]*n
        stack1=[]
        stack2=[]
        for i in range(n):
            while stack1 and arr[stack1[-1]]<arr[i]:
                stack1.pop()
            prev_larg[i]=stack1[-1] if stack1 else -1
            stack1.append(i)
            while stack2 and arr[stack2[-1]]<arr[n-1-i]:
                stack2.pop()
            next_larg[n-1-i]=stack2[-1] if stack2 else n
            stack2.append(n-1-i)
        ans=0
        for i in range(n):
            ans=max(ans,next_larg[i]-prev_larg[i]-1)
        return ans