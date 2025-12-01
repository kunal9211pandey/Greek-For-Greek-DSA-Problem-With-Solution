#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        if not arr:
            return None
        head = None
        tail = None
        
        for val in arr:
            new_node = Node(val)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node
        return head