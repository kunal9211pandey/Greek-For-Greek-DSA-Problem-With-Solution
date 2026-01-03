#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        for ch in range(len(s)-1 , -1 ,-1):
            if s[ch] == '1':
                return ch
        return -1
