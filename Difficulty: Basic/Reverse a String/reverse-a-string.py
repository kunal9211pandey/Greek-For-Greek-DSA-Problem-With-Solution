#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        char_list = list(s)
        i = 0
        j = len(s)-1
        
        while i < j:
            char_list[i], char_list[j] = char_list[j], char_list[i]
            i += 1
            j -= 1
        return "".join(char_list)