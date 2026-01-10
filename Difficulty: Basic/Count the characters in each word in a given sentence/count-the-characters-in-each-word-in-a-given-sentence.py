#User function Template for python3

class Solution:
    def countChars(self,s):
        # code here 
        result = []
        count = 0
        
        for ch in s:
            if ch != ' ':
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
        return result
