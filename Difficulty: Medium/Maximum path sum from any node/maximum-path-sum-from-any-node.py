#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        lt = [-10000000000]
        mx = self.sol(root,lt)
        mr = max(lt)
        return max(mr,mx)
    def sol(self,root,lt):
        if root.left == None and root.right == None:
            return root.data
        else:
            m1 = -10000000000
            m2 = -10000000000
            if root.left != None:
                m1 = self.sol(root.left,lt)
                
            if root.right != None:
                m2 = self.sol(root.right,lt)
                
            
            lt.append(max(m1+m2+root.data,m1,m2))
            return max(m1+root.data,m2+root.data,root.data)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Suman Rana
import sys
sys.setrecursionlimit(100000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        ob = Solution()
        print(ob.findMaxSum(root))
        
        

        print("~")
# } Driver Code Ends