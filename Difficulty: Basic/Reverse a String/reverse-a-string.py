#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        n = len(s)
        reversed_str = ""
        for i in range(n - 1, -1, -1):  # Iterate from last index to first
            reversed_str += s[i]
        return reversed_str
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends