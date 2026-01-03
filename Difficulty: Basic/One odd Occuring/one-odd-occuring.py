class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        result = 0
        
        for num in arr:
            result ^= num
        return result