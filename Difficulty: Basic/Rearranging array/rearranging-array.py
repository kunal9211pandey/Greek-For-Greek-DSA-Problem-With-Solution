#User function Template for python3

class Solution:    
    def Rearrange(self, arr):
        #Code Here
        result = []
        arr.sort()
        left = 0
        right = len(arr)-1
        
        while left <= right:
            if left == right:
                result.append(arr[left])
            else:
                result.append(arr[left])
                result.append(arr[right])
            left += 1
            right -= 1

        return result