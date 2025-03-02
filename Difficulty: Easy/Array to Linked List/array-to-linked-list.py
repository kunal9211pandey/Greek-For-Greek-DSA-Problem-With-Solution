#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Node Class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Solution:
    def constructLL(self, arr):
        # code here
        if not arr:
            return None
        
        head=Node(arr[0])
        current=head
        for i in arr[1:]:
            current.next=Node(i)
            current = current.next
        
        return head
    
    def printLL(head):
        current=head
        
        while current:
            print(data , end='->'if current.next else "\n")
            current=current.next
            


#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
        print("~")
# } Driver Code Ends