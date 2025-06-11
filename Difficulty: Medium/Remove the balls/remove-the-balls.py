#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack=[]
        for c,r in zip(color,radius):
            if stack and (stack[-1][0]==c and stack[-1][1]==r):
                stack.pop()
            else:
                stack.append([c,r])
        
        return len(stack)