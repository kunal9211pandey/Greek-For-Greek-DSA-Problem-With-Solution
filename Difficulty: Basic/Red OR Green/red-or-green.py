#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        #code here
        R = 0
        G = 0
        for ch in S:
            if ch == 'R':
                R += 1
            elif ch =='G':
                G += 1
        if R > G:
            return G
        elif G < R:
            return R
        else:
            return min(R,G)
        
                