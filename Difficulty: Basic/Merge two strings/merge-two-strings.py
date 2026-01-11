#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        i = 0
        j = 0
        result = []
        
        while i < len(S1) and j < len(S2):
            result.append(S1[i])
            result.append(S2[j])
            i += 1
            j += 1
        while i < len(S1):
            result.append(S1[i])
            i += 1
        while j < len(S2):
            result.append(S2[j])
            j += 1
        return "".join(result)