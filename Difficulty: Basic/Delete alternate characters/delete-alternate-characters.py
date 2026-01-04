#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        # code here 
        result = ""
        for i in range(len(S)):
            if i % 2 ==0:
                result += S[i]
        return result