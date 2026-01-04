#User function Template for python3
class Solution:
    def URLify(self, s): 
        result = ''
        for ch in s:
            if ch == ' ':
                result += '%20'
            else:
                result += ch
        return result