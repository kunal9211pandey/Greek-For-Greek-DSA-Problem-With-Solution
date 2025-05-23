#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest = second_largest = -1
        
        for num in arr:
            if num>largest:
                second_largest=largest
                largest=num
                
            elif num>second_largest and num != largest:
                second_largest=num
                
        return second_largest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends