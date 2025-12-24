#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,node):
        # code here
        if node is None:
            return []
        s1 = []
        s2 = []
        
        s1.append(node)
        
        while s1:
            current = s1.pop()
            s2.append(current.data)
            
            if current.left:
                s1.append(current.left)
                
            if current.right:
                s1.append(current.right)
        
        return s2[::-1]
            