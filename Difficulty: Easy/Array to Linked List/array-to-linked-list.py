'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        # code here
        if not arr:
            return None
            
        head = Node(arr[0])
        current = head
        
        for val in arr[1:]:
            current.next = Node(val)
            current = current.next
        return head
        
    def print_ll(head):
        current = head
        while current:
            print(current.data , end ="->" if current.next else "\n")
        
        
        