class Solution:
    def maxSum(self, arr):
        # code here
        max_sum = float('-inf')
        
        for i in range(len(arr)-1):
            current_sum = arr[i] + arr[i+1]
            max_sum = max(current_sum , max_sum)
        return max_sum
