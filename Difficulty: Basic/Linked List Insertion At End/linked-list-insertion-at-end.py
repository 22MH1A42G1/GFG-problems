'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        new = Node(x)
        if not head: return new
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new
        return head
        