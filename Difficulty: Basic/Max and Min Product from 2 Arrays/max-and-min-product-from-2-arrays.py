#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        # code here
        max_val = arr1[0]
        min_val = arr2[0]
        
        for x in arr1:
            if x > max_val:
                max_val = x
                
        for y in arr2:
            if y < min_val:
                min_val = y
                
        return max_val * min_val
