#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        max_element=arr[0]
        min_element=arr[0]
        n=len(arr)
        for i in range(1,n):
            if arr[i]>max_element:
                max_element=arr[i]
            if arr[i]<min_element:
                min_element=arr[i]
                
        return min_element , max_element
            
    


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")


# } Driver Code Ends