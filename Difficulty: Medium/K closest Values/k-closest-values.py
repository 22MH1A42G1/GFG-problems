'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def InorderTraversal(self, root, target, k, res):
        if not root: return
        self.InorderTraversal(root.left, target, k, res)
        if len(res) < k: res.append(root.data)
        elif abs(target - res[0]) > abs(target - root.data):
            res.append(root.data)
            res.pop(0)
        self.InorderTraversal(root.right, target, k, res)
    def getKClosest(self, root, target, k):
        # code here
        res = []
        self.InorderTraversal(root,target,k,res)
        return res
    