"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if head is None or head.next is None:
            return head
        
        current = head
        new_head = None
        
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            new_head = current
            current = current.prev
        return new_head
        
        