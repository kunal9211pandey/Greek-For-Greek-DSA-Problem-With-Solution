"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        if head is None or x <= 0:
            return head

        # delete head position
        if x == 1:
            nxt = head.next
            if nxt:
                nxt.prev = None
            return nxt

        current = head
        count = 1

        # reach the x-th node
        while current and count < x:
            current = current.next
            count += 1

        # if x > length
        if current is None:
            return head

        # unlink current node
        if current.prev:
            current.prev.next = current.next

        if current.next:
            current.next.prev = current.prev

        return head
        
        
        
        