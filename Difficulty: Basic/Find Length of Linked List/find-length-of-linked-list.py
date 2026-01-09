'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        c=0
        temp = head
        while temp:
            c+=1
            temp=temp.next
        return c