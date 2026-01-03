class Solution:
    def find_unique(self, k, arr):
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key in freq:
            if freq[key] % k != 0:
                return key
