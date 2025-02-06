#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        m = {val: idx for idx, val in enumerate(inorder)}
        pi = [0] 
        def f(s, e):
            if s > e:
                return None
            v = preorder[pi[0]]
            root = Node(v)
            pi[0] += 1
            pos = m[v]
            root.left = f(s, pos - 1)
            root.right = f(pos + 1, e)
            return root
        
        return f(0, len(inorder) - 1)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends