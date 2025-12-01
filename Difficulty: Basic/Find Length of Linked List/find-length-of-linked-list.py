'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count