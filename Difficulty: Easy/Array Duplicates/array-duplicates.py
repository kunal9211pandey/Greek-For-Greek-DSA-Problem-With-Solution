class Solution:
    def findDuplicates(self, arr):
        # code here
        arr.sort()
        
        i = 0
        j = 1
        result = []
        while i < len(arr)-1:
            if arr[i] == arr[j]:
                result.append(arr[i])
            i += 1
            j += 1
        return result