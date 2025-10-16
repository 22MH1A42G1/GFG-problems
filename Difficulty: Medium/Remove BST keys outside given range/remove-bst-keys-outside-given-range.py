'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        #code here
        def dfs(cur=root):
            nonlocal l,r
            if not cur:
                return None
            if l<=cur.data<=r:
                cur.left=dfs(cur.left)
                cur.right=dfs(cur.right)
                return cur
            if cur.data<l:
                return dfs(cur.right)
            if cur.data>r:
                return dfs(cur.left)
        return dfs()