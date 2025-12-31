'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        s = set()
        while head1:
            s.add(head1)
            head1=head1.next
        while head2:
            if head2 in s:
                return head2
            head2=head2.next
            