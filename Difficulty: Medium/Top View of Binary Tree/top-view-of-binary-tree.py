'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        # code here
        if not root:
            return []
        q = deque()
        q.append((root,0))
        mp = {}
        while q:
            node, hd = q.popleft()
            if hd not in mp:
                mp[hd] = node.data
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
        ans = [mp[k] for k in sorted(mp.keys())]
        return ans