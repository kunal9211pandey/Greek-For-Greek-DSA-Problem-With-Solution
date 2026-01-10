#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        result = []
        for ch in str1:
            if ch not in str2:
                result.append(ch)
        return "".join(result)