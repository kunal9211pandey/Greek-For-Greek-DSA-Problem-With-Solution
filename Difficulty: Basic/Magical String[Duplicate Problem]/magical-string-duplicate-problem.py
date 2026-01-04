#User function Template for python3
class Solution:
    def magicalString (ob,S):
        # code here 
        result = []
        
        for ch in S:
            magic = chr(ord('a') + ord('z') - ord(ch))
            result.append(magic)
        return "".join(result)