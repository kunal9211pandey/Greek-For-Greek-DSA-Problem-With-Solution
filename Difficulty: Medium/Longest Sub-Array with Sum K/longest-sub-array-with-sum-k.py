# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        # code here
        cum_sum=0
        max_len=0
        cum_sum_map={}
        n=len(arr)
        for i in range(n):
            cum_sum+=arr[i]
            
            if cum_sum == k:
                max_len = i+1
            
            if (cum_sum-k) in cum_sum_map:
                max_len=max(max_len ,i-cum_sum_map[cum_sum-k])
            
            if cum_sum not in cum_sum_map:
                cum_sum_map[cum_sum]=i
        
        return max_len
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends