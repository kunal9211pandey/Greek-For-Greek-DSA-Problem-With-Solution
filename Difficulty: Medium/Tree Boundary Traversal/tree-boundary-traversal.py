'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        boundary = []

        def isleaf(node):
            return not node.left and not node.right

        # Add root (only once)
        if not isleaf(root):
            boundary.append(root.data)

        # 1. Add Left Boundary (excluding leaves)
        def addLeftBoundary(node):
            current = node.left
            while current:
                if not isleaf(current):
                    boundary.append(current.data)
                if current.left:
                    current = current.left
                else:
                    current = current.right

        # 2. Add Leaf Nodes
        def addLeaves(node):
            if not node:
                return
            if isleaf(node):
                boundary.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)

        # 3. Add Right Boundary (excluding leaves, reversed)
        def addRightBoundary(node):
            current = node.right
            stack = []
            while current:
                if not isleaf(current):
                    stack.append(current.data)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            while stack:
                boundary.append(stack.pop())

        if root.left:
            addLeftBoundary(root)

        addLeaves(root)

        if root.right:
            addRightBoundary(root)

        return boundary
