#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        count = 0
        for ch in s:
            if 'A'<= ch <= 'Z':
                count += 1
        return count