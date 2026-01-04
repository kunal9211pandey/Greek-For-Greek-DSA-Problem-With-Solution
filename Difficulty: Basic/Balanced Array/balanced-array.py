#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        n = len(arr)
        mid = n // 2
        
        left_sum = 0
        right_sum = 0
        
        
        for i in range(0 , mid):
            left_sum += arr[i]
            
        for j in range(mid , n):
            right_sum += arr[j]
            
        return abs(left_sum - right_sum)