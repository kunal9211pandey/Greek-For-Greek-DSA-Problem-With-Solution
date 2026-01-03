
class Solution:
    def swapKth(self, arr, k):
        # Code Here
        n = len(arr)
        
        index1 = k -1
        index2 = n-k
        
        arr[index1], arr[index2] = arr[index2], arr[index1]
        
        return arr
        
