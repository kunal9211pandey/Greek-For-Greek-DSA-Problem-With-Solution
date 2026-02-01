class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        current_sum = 0
        n = len(arr)
        
        for i in range(k):
            current_sum += arr[i]
        max_sum = current_sum
        
        for i in range(k,n):
            current_sum += arr[i]
            current_sum -= arr[i-k]
            max_sum = max(current_sum, max_sum)
        return max_sum