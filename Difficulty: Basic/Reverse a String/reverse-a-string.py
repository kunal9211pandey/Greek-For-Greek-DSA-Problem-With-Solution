#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        char = list(s)
        i = 0
        j = len(char)-1
        
        while i < j:
            char[i] , char[j] = char[j] , char[i]
            i += 1
            j -= 1
        return "".join(char)