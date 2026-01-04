#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        prod = 1
        
        for i in range(len(arr)):
            prod = arr[i] * prod
        return prod
    
