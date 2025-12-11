#User function Template for python3

class Solution:
    def createTree(self, root, l):
        # Code here
        if not l:
            return
        
        if len(l)<2:
            return root
        
        
        queue = [root]
        i = 1
        
        while i < len(l):
            current = queue.pop(0)
            
            if i < len(l):
                current.left = Node(l[i])
                queue.append(current.left)
                i+=1
                
            if i < len(l):
                current.right = Node(l[i])
                queue.append(current.right)
                i+=1