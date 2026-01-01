#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        count = 0
        
        for num in arr:
            if num <= x:
                count += 1
        return count

