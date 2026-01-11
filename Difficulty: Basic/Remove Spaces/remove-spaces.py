#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        result = []
        for ch in s:
            if ch != ' ':
                result.append(ch)
        return "".join(result)