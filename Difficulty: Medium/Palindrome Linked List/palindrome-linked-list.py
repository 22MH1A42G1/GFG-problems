'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        def check(n):
            nonlocal head
            if not n:
                return True
            r = check(n.next) and n.data == head.data
            head = head.next
            return r
        
        return check(head)
        